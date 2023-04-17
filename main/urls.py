from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPage"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]