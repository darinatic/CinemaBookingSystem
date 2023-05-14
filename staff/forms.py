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