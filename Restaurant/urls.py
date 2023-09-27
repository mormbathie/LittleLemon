#define URL route for index() view
from django.db import router
from django.urls import path
from . import views
from .views import BookingViewSet, UserViewSet  
from rest_framework.authtoken.views import ObtainAuthToken
# router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    # path('', views.index, name='index'),
    path('menu-items/', views.BookingViewSet.as_view()),
    # path('api-token-auth/', obtain_auth_token),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('booking-table/', BookingViewSet.as_view(), name='booking-table-list-create'),
    path('menu-table/', UserViewSet.as_view(), name='menu-table-list-create'),

]
