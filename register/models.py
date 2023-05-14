from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user_profile_name}'

class User(AbstractUser):
    
    user_type_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

