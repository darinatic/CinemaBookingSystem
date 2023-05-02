from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPage"),
    path("home/", views.mainPage, name="home"),
    path("movie_details/<int:movie_id>", views.movie_details, name="movie_details"),
    path('addtoCart/', views.addtoCart, name='addtoCart'),
    path('ticketcart/', views.ticketcart, name='ticketcart'),
    path('updateCart/', views.updateCart, name='updateCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]