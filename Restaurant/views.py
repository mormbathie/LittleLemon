from .models import BookingTable, MenuTable
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here. 

class BookingViewSet(generics.ListCreateAPIView):
    permission_classes = [ IsAuthenticated ]
    queryset = BookingTable.objects.all() 
    serializer_class = BookingSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuTable.objects.all()
    serializer_class=MenuSerializer
    permission_classes=[IsAuthenticated]

class UserViewSet(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   authentication_classes = [TokenAuthentication]  
   permission_classes = [IsAuthenticated]
   