from django.shortcuts import render, redirect, reverse
from .models import Movie
from django.http import HttpResponseRedirect

# Create your views here.
def mainPage(response):
   
    if not response.user.is_authenticated:
        return redirect ("/login")
    
    if response.method == 'POST' and response.POST.get('addMovie'):
        m = Movie()
        m.save()

        return redirect(reverse('home'))

    movies = Movie.objects.all()
    return render(response, 'CinemaCustomerPages/home.html', {'movies': movies})

def movie_details(response, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    return render(response, 'CinemaCustomerPages/movie_detail.html', {'movie': movie})

def test(response):
    return render(response, 'CinemaCustomerPages/movie_detail.html', {})