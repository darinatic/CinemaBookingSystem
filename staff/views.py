from django.shortcuts import render, redirect
from main.models import *
from django.db.models import Q
from staff.forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def ticket_list(request):
    query = request.GET.get('q')
    if query:
        tickets = Ticket.objects.filter(user_id__username__icontains=query)
    else:
        tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket Booked successfully')
            return redirect('ticket_list')
        else:
            print(form.errors)
    else:
        form = TicketForm(user=request.user)
    return render(request, 'ticket_create.html', {'form': form})

def get_seats(request, movie_session_id):
    seats = Seat.objects.filter(session_id=movie_session_id, is_available=True)
    seat_data = [{'id': seat.seat_id, 'seat_row': seat.seat_row, 'seat_number': seat.seat_number} for seat in seats]

    return JsonResponse({'seats': seat_data})

def ticket_update_multiple(request):
    if request.method == 'POST':
        form = TicketUpdateMultipleForm(request.POST)
        if form.is_valid():
            selected_tickets = form.cleaned_data['selected_tickets']
            Ticket.objects.filter(ticket_id__in=selected_tickets).update(is_paid=True)
            messages.success(request, 'Tickets updated successfully')
            return redirect('ticket_list')
        else:
            print(form.errors)
    else:
        form = TicketUpdateMultipleForm()
    return render(request, 'ticket_update_multiple.html', {'form': form}) 

cart = []  # Initialize cart
def purchase_food_and_drinks(request):
    total_cost = 0  # Initialize total cost
    
    if request.method == 'POST':
        form = FoodAndDrinksForm(request.POST)
        if form.is_valid():
            # Get the combo name and quantity and price
            combo_name = form.cleaned_data['combo_name']
            combo_price = FoodAndDrinks.objects.get(combo_name=combo_name).combo_price
            quantity = form.cleaned_data['quantity']

            # Calculate the total cost for 1 item
            item_total = combo_price * quantity

             # Create a new dictionary representing the selected item
            selected_item = {
                'combo_name': combo_name,
                'quantity': quantity,
                'price': item_total,
            }
            cart.append(selected_item)
            
            messages.success(request,  f'{combo_name} added to cart')
            # return redirect('purchase_food_and_drinks')
    else:
        form = FoodAndDrinksForm()

    # Calculate the total cost for all items in the cart
    for item in cart:
        total_cost += item['price']

    context = {
        'form': form,
        'cart': cart,
        'total_cost': total_cost,
    }
    return render(request, 'purchase_food_and_drinks.html', context)

def reset_cart(request):
    global cart
    cart = []
    messages.success(request, 'Cart has been reset')
    return redirect('purchase_food_and_drinks')

def remove_item(request, index):
    if request.method == 'POST':
        # Remove the item from the cart based on the given index
        if index < len(cart):
            del cart[index]
            messages.success(request, 'Item removed from cart.')
        else:
            messages.error(request, 'Invalid item index.')
    return redirect('purchase_food_and_drinks')

def food_and_drinks_checkout(request):
    cart.clear()
    messages.success(request, 'Checkout successful')
    return redirect('purchase_food_and_drinks')

def get_combo_price(request, combo_name):
    try:
        food_and_drinks = FoodAndDrinks.objects.get(combo_id=combo_name)
        combo_price = food_and_drinks.combo_price
        return JsonResponse({'combo_price': combo_price})
    except FoodAndDrinks.DoesNotExist:
        return JsonResponse({'error': 'Combo not found'}, status=404)