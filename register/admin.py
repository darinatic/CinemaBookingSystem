from django.contrib import admin
from .models import User, UserProfile
from main.models import Ticket

#   DO NOT REPLACE THE FOLLOWING!
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile_name')
    list_filter = ('id', 'user_profile_name')
    search_fields = ('id', 'user_profile_name')
    ordering = ('id', 'user_profile_name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type_id')
    list_filter = ('user_type_id',)
    search_fields = ('username', 'email')
    ordering = ('username', 'email', 'user_type_id')

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
