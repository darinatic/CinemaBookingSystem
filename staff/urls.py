from django.urls import path
from . import views

urlpatterns = [
    # ticket list
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket_create/', views.ticket_create, name='ticket_create'),
    path('get_seats/<int:movie_session_id>/', views.get_seats, name='get_seats'),
    path('ticket/update_multiple/', views.ticket_update_multiple, name='ticket_update_multiple'),
]