from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_tag1'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_tag2'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_tag3'}),
        }
        