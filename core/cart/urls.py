from django.contrib import admin
from django.urls import include, path



urlpatterns = [
path('api/v1/' , include('cart.api.v1.urls'))
    
]