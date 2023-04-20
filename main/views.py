from django.shortcuts import render, redirect
from .models import Movie
from django.http import HttpResponseRedirect

# Create your views here.
def mainPage(response):
   
    if not response.user.is_authenticated:
        return redirect ("/login")
    
    if response.POST.get("addMovie"):
        m = Movie()
        m.save()
        movies = Movie.objects.all()
        return render(response, "CinemaCustomerPages/home.html", {"movies": movies})
        
    return render(response, "CinemaCustomerPages/home.html")
