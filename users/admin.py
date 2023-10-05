from django.contrib import admin
from .models import Users
from products.admin import OrdersAdmin
# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'id')
    search_fields = ('username', 'phone_number', 'email', 'first_name', 'last_name')
    fields = ('image', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'is_staff', 'is_active', 'is_superuser',
              'last_login', 'date_joined', ('groups', 'user_permissions'))
    # readonly_fields = ('password',)
    inlines = [OrdersAdmin]