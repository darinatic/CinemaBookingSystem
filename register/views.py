from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = RegisterForm(response.POST)
    return render(response, "user_register/register.html", {"form" : form})

        
