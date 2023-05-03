from django.shortcuts import render, redirect, reverse
from .models import Movie, MovieSession, CinemaRoom, Ticket
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers
import json

# Create your views here.
def mainPage(response):
   
    if not response.user.is_authenticated:
        return redirect ("/login")
    
    if response.method == 'POST' and response.POST.get('addMovie'):
        m = Movie()
        m.save()

        return redirect(reverse('home'))

    if CinemaRoom.objects.count() == 0:
        cr = CinemaRoom.objects.create(room_name="Room 1")
        cr.save()
           
    movies = Movie.objects.all()
    
    for movie in movies:    
        if MovieSession.objects.filter(movie_id = movie).count() == 0:
            movie_session = MovieSession (movie_id= movie, room_id = CinemaRoom.objects.get(room_id = 1), start_time = datetime.now())
            movie_session.save()
    
    sessions = MovieSession.objects.select_related('movie_id').all().values('movie_id__movie_id', 'movie_id__movie_title', 'movie_id__movie_duration', 'movie_id__movie_genre','movie_id__movie_img', 'movie_id__movie_description' ,'movie_id__is_active', 'room_id__room_id', 'room_id__room_name', 'start_time')
    sessions_list = list(sessions)
    
    for session in sessions_list:
        session['start_time'] = session['start_time'].strftime("%Y-%m-%d %H:%M:%S")
    sessions_json = json.dumps(sessions_list)
    return render(response, 'CinemaCustomerPages/home.html', {'movies': movies,'sessions' : sessions , 'sessions_json': sessions_json})


def movie_details(response, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    movie_json = json.dumps(model_to_dict(movie))
    return render(response, 'CinemaCustomerPages/movie_detail.html', {'movie': movie,'movie_json': movie_json})

def addtoCart(request):
    data = request.GET.get("data")
    request.session["cart"] = data
    return redirect("/ticketcart")
    
def ticketcart(request):
    data = request.session.get("cart")
    tickets = json.loads(data) if data else [] 
    context = {"tickets": json.dumps(tickets)}
    
    return render(request, "CinemaCustomerPages/ticketcart.html", context)

@csrf_exempt
def updateCart(request):
    if request.method == "POST":
        data = request.POST.get("data")
        request.session["cart"] = data
        request.session.save()
        return redirect("/ticketcart")
    
def checkout(request):
    data = request.GET.get("data")
    tickets = json.loads(data) if data else []
    return render(request, "CinemaCustomerPages/myPurchasedTickets.html", {"tickets" : json.dumps(tickets)})

def purchaseTickets(request):
    pass



