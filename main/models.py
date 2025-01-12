# from django.contrib.auth.models import AbstractUser 
from django.db import models
from register.models import User
from datetime import datetime
from PIL import Image
from django.utils import timezone

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_avatars', default='avatar.jpg')
    seat_preference = models.CharField(max_length=50, default='Front')
    loyalty_points = models.IntegerField(default=0)
    

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

class Movie(models.Model): 
    
    JOHN_WICK_IMAGE = "data:image/jpeg;base64,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"
    
    movie_id = models.AutoField(primary_key=True, unique=True, auto_created=True, null=False) 
    movie_title = models.CharField(max_length=200, default="John Wick")
    movie_description = models.TextField(max_length=250, default="John is very angry")
    movie_genre = models.CharField(max_length=50, default="Action") 
    movie_duration = models.FloatField(max_length=20,default=2)
    movie_img = models.TextField(default=JOHN_WICK_IMAGE)
    is_active = models.BooleanField(default=True)
 
    def __str__(self): 
        return f'{self.movie_title}' 
     
class FoodAndDrinks(models.Model):
    combo_id = models.AutoField(primary_key=True)
    combo_name = models.CharField(max_length=50, default="Popcorn and Coke")
    combo_price = models.FloatField(max_length=20, default=10)

    def __str__(self):
        return f'{self.combo_name}'
     
class CinemaRoom(models.Model): 
    room_id = models.AutoField(primary_key=True, auto_created=True, null=False) 
    room_name = models.CharField(max_length=20, default="Room 1")
    total_seat = models.IntegerField(default=100)
    
    def __str__(self): 
        return f'{self.room_name}' 
    
    def __str__(self): 
        return self.room_name
    
    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk and not Seat.objects.filter(room_id=self).exists():
            self.create_seats()
            
    def create_seats(self):
        for i in range(self.total_seat):
            seat = Seat(room_id=self, seat_number=i+1, seat_row = i//10 + 1)
            seat.save()
     
class RatingAndReview(models.Model): 
    review_id = models.AutoField(primary_key=True) 
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField() 
    review = models.TextField(max_length=250) 
 
    def __str__(self): 
        return f'{self.user_id.username}, {self.rating}' 
     
# class MovieSession(models.Model): 
#     session_id = models.AutoField(primary_key=True, auto_created=True, null=False) 
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE) 
#     room_id = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE) 
#     start_time = models.DateTimeField(default=datetime.now())
 
#     def __str__(self): 
#         return f'{self.room_name}'
    
class MovieSession(models.Model):   
    session_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room_id = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return f'{self.movie_id.movie_title} in {self.room_id.room_name} at {self.start_time}'
    
class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey('CinemaRoom', on_delete=models.CASCADE)
    session_id = models.ForeignKey('MovieSession', null=True, on_delete=models.SET_NULL)
    seat_row = models.CharField(max_length=1)
    seat_number = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)

    def update_availability(self):
        if not self.is_available and self.session_id is not None and self.session_id.start_time + timezone.timedelta(hours=3) < timezone.now():
            self.is_available = True
            self.save()

    def __str__(self):
        return f'{self.room_id.room_name} {self.seat_row}-{self.seat_number}'

class Ticket(models.Model): 
    ticket_id = models.AutoField(primary_key=True) 
    ticket_type = models.CharField(max_length=20, default="Adult")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    movie_session = models.ForeignKey(MovieSession, on_delete=models.CASCADE) 
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE) 
    combo_id = models.ForeignKey(FoodAndDrinks, null=True, on_delete=models.CASCADE) 
    cost = models.FloatField(null=True)
    purchased_date = models.DateTimeField(default=datetime.now())
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only update seat availability for new tickets
            self.seat_id.is_available = False
            self.seat_id.save()
        if not self.purchased_date:  # Set default value for purchased_date if not provided
            self.purchased_date = timezone.now()
        super().save(*args, **kwargs)
 
    def __str__(self): 
        return f'{self.user_id.username}, {self.movie_session.movie_id.movie_title}, {self.ticket_type}'    

    