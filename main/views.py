from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Movie, MovieSession, CinemaRoom, Ticket, Seat
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
        if MovieSession.objects.filter(movie_id = movie).count() == 0 and movie.is_active == True:
            movie_session = MovieSession (movie_id= movie, room_id = CinemaRoom.objects.get(room_id = 1), start_time = datetime.now())
            movie_session.save()
    
    sessions = MovieSession.objects.select_related('movie_id').all().values('session_id','movie_id__movie_id', 'movie_id__movie_title', 'movie_id__movie_duration', 'movie_id__movie_genre','movie_id__movie_img', 'movie_id__movie_description' ,'movie_id__is_active', 'room_id__room_id', 'room_id__room_name', 'start_time')
    sessions_list = list(sessions)
    
    for session in sessions_list:
        session['start_time'] = session['start_time'].strftime("%Y-%m-%d %H:%M:%S")
    sessions_json = json.dumps(sessions_list)
    return render(response, 'CinemaCustomerPages/home.html', {'movies': movies,'sessions' : sessions , 'sessions_json': sessions_json})


def movie_details(response, session_id):
    
    session = MovieSession.objects.select_related('movie_id','room_id').get(session_id=session_id)
    movie = session.movie_id
    room = session.room_id
    session_dict = model_to_dict(session)
    session_dict['start_time'] = session_dict['start_time'].strftime("%Y-%m-%d %H:%M:%S")
    session_dict['movie'] = model_to_dict(movie)
    session_dict['room'] = model_to_dict(room)
    
    
    seats = list (Seat.objects.filter(room_id = room).values('seat_id', 'seat_row', 'seat_number', 'is_available'))
    
    for seat in seats:
        seat['session_id'] = session_id
    
    session_dict['seats'] = seats
    
    session_json = json.dumps(session_dict)
    
    return render(response, 'CinemaCustomerPages/movie_detail.html', {'movie': movie,'session_json': session_json})
    
def addtoCart(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data.get("data")
        request.session["cart"] = data
        return HttpResponse("OK")
    
def ticketcart(request):
    data = request.session.get("cart")
    tickets = json.loads(json.dumps(data)) if data else [] 
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
    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data.get("data")
        request.session["checkout"] = data
        return HttpResponse("OK")
        
def checkOutCart(request):
    data = request.session.get("checkout")
    tickets = json.loads(json.dumps(data)) if data else []
    context = {"tickets": json.dumps(tickets)}
    return render(request, "CinemaCustomerPages/myPurchasedTickets.html", context)

def purchaseTickets(request):
    pass

def test(request, session_id):
    session = MovieSession.objects.get(session_id=session_id)
    movie = session.movie_id
    print(movie)
    session.movie = movie
    session.start_time = session.start_time.strftime("%Y-%m-%d %H:%M:%S")
    session_json = json.dumps(model_to_dict(session))
    return render(request, 'CinemaCustomerPages/test.html', {'session': session,'session_json': session_json})


def mainPageAlter(request):
    return render (request, 'CinemaCustomerPages/homealternative.html')
