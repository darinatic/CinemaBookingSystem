from django.contrib import admin
from .models import *
from register.models import User

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'movie_genre', 'movie_duration') # Customize the fields displayed in the list view
    search_fields = ('movie_title', 'movie_genre') # Add search functionality for these fields
    list_filter = ('movie_genre',)
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Seat)
admin.site.register(CinemaRoom)
admin.site.register(RatingAndReview)
admin.site.register(MovieSession)
admin.site.register(FoodAndBeverage)
admin.site.register(Ticket)