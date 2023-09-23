from django.contrib import admin
from .models import BookingTable
from .models import MenuTable

admin.site.register(BookingTable)
admin.site.register(MenuTable)

# Register your models here.
