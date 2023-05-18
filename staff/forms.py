from typing import Any, Dict
from django import forms
from django.utils import timezone
from main.models import *

class TicketForm(forms.ModelForm):
    TICKET_TYPE_CHOICES = (
        ('Adult', 'Adult'),
        ('Child', 'Child'),
        ('Senior', 'Senior'),
    )
    ticket_type = forms.ChoiceField(choices=TICKET_TYPE_CHOICES, required=True)
    movie_session = forms.ModelChoiceField(queryset=MovieSession.objects.all(), required=True)
    seat_id = forms.ModelChoiceField(queryset=Seat.objects.filter(is_available=True), required=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['combo_id', 'purchased_date', 'is_paid']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user_id'].initial = user.id
            self.fields['user_id'].widget = forms.HiddenInput()
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['purchased_date'] = datetime.now()
        cleaned_data['combo_id'] = None
        cleaned_data['is_paid'] = True

        return cleaned_data
    
    
class TicketUpdateMultipleForm(forms.Form):
    selected_tickets = forms.ModelMultipleChoiceField(
        queryset=Ticket.objects.all(),
        widget=forms.CheckboxSelectMultiple
)

class FoodAndDrinksForm(forms.Form):
    combo_name = forms.ModelChoiceField(queryset=FoodAndDrinks.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    combo_price = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['combo_price'].initial = self.initial.get('combo_price', '')

    def clean(self):
        cleaned_data = super().clean()
        combo_name = cleaned_data.get('combo_name')
        if combo_name:
            food_and_drinks = FoodAndDrinks.objects.filter(combo_name=combo_name).first()
            if food_and_drinks:
                cleaned_data['combo_price'] = food_and_drinks.combo_price
        return cleaned_data
