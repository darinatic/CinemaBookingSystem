from django import forms
from main .models import CinemaRoom, FoodAndBeverage, Movie, MovieSession, Ticket, Seat

class CinemaRoomForm(forms.ModelForm):
    room_name = forms.CharField(label='Name')
    total_seat = forms.IntegerField(label='Total Seats')
    class Meta:
        model = CinemaRoom
        fields = '__all__'

class FoodAndDrinksForm(forms.ModelForm):
    combo_name = forms.CharField(label='Name')
    combo_price = forms.DecimalField(label='Price')
    class Meta:
        model = FoodAndBeverage
        fields = '__all__'

class MovieForm(forms.ModelForm):
    # movie_title = forms.CharField(label='Title')
    # movie_duration = forms.IntegerField(label='Duration')
    # movie_genre = forms.CharField(label='Genre')
    # is_active = forms.ChoiceField(choices=((True, 'Active'), (False, 'Inactive')))
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSessionForm(forms.ModelForm):
    movie_id = forms.ModelChoiceField(queryset=Movie.objects.filter(is_active=True), label='Movie')
    room_id = forms.ModelChoiceField(queryset=CinemaRoom.objects.all(), label='Room')
    class Meta:
        model = MovieSession
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SeatForm(forms.ModelForm):
    room_id = forms.ModelChoiceField(queryset=CinemaRoom.objects.all(), label='Room')
    session_id = forms.ModelChoiceField(queryset=MovieSession.objects.all(), label='Session')
    # is_availabe = forms.ChoiceField(choices=((True, 'Available'), (False, 'Unavailable')))
    class Meta:
        model = Seat
        fields = '__all__'

class ReportForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Start Date')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='End Date')



