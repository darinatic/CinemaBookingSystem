from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type_id')
    list_filter = ('user_type_id',)
    search_fields = ('username', 'email')
    ordering = ('username', 'email', 'user_type_id')
admin.site.register(User, UserAdmin)