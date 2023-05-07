from django.shortcuts import render

def view_username(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Unregistered"
    return {'current_user': username}

