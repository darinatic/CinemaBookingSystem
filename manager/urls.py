from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # logout
    path('logout/', views.my_logout, name='logout'),

    # main page
    path('manager_home/', views.manager_home, name='manager_home'),

    # user profile
    path('user_profile/', views.user_profile, name='user_profile'),

    # report page
    path('report_page/', views.report_page, name='report_page'),

    # cinema room
    path('cinema_room_create/', views.create_cinema_room, name='cinema_room_create'),
    path('cinema_room_list/', views.cinema_room_list, name='cinema_room_list'),
    path('cinema_room_update/<int:pk>/', views.update_cinema_room, name='cinema_room_update'),

    # food and drinks
    path('food_and_drinks_create/', views.food_and_drinks_create, name='food_and_drinks_create'),
    path('food_and_drinks_list/', views.food_and_drinks_list, name='food_and_drinks_list'),
    path('food_and_drinks_update/<int:pk>/', views.food_and_drinks_update, name='food_and_drinks_update'),
    path('food_and_drinks_delete/<int:pk>/', views.food_and_drinks_delete, name='food_and_drinks_delete'),

    # movie
    path('movie_create/', views.movie_create, name='movie_create'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_update/<int:pk>/', views.movie_update, name='movie_update'),

    # movie session
    path('movie_session_create/', views.movie_session_create, name='movie_session_create'),
    path('movie_session_list/', views.movie_session_list, name='movie_session_list'),
    path('movie_session_update/<int:pk>/', views.movie_session_update, name='movie_session_update'),
    path('movie_session_delete/<int:pk>/', views.movie_session_delete, name='movie_session_delete'),

    # seat
    path('seat_create/', views.seat_create, name='seat_create'),
    path('seat_list/', views.seat_list, name='seat_list'),
    path('seat_update/<int:pk>/', views.seat_update, name='seat_update'),
    path('seat_delete/<int:pk>/', views.seat_delete, name='seat_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)