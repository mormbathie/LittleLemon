from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BookingTable, MenuTable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
     

     class Meta:
        model = MenuTable
        fields = ['id', 'Title', 'Price', 'Inventory']
