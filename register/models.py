from django.db import models
from django.contrib.auth.models import AbstractUser

# DO NOT REPLACE THE FOLLOWING MODELS IF THERE IS ANY DATABASE ERROR WHEN MIGRATING, 
# READ THE README.md FILE FOR MORE INFORMATION
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile_name = models.CharField(max_length=50)
    suspend = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_profile_name}'

class User(AbstractUser):
    user_type = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
