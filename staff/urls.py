from django.urls import path
from . import views
import staff.views

urlpatterns = [
    # ticket list
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket_create/', views.ticket_create, name='ticket_create'),
    path('get_seats/<int:movie_session_id>/', views.get_seats, name='get_seats'),
    path('ticket/update_multiple/', views.ticket_update_multiple, name='ticket_update_multiple'),
    path('purchase-food-and-drinks/', views.purchase_food_and_drinks, name='purchase_food_and_drinks'),
    path('get_combo_price/<int:combo_name>/', views.get_combo_price, name='get_combo_price'),
    path('reset_cart/', views.reset_cart, name='reset_cart'),
    path('remove_item/<int:index>/', views.remove_item, name='remove_item'),
    path('food_and_drinks_checkout/', views.food_and_drinks_checkout, name='food_and_drinks_checkout'),
]