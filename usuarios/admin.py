from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'address', 'number', 'city', 'cc', 'last_login', 'date_joined')