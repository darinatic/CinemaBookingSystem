from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPage"),
    path("home/", views.mainPage, name="home"),
    path("movie_details/<int:movie_id>", views.movie_details, name="movie_details"),
    path('test/', views.test, name='test'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]