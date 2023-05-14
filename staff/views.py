from django.shortcuts import render, redirect
from main.models import *
from django.db.models import Q
from staff.forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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