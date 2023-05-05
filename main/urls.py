from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPage"),
    path("home/", views.mainPage, name="home"),
    path("homealter/", views.mainPageAlter, name="homealter"),
    path("movie_details/<int:session_id>", views.movie_details, name="movie_details"),
    path("test/<int:session_id>", views.test, name="test"),
    path('addtoCart/', views.addtoCart, name='addtoCart'),
    path('ticketcart/', views.ticketcart, name='ticketcart'),
    path('updateCart/', views.updateCart, name='updateCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkOutCart/', views.checkOutCart, name='checkOutCart'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]