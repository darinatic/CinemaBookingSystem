from django.shortcuts import render, redirect, reverse
from .models import Movie, MovieSession, CinemaRoom, Ticket
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
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
        
    sessions = MovieSession.objects.all()
    return render(response, 'CinemaCustomerPages/home.html', {'movies': movies, 'sessions': sessions})

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



