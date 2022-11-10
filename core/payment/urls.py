from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('request/<int:cart_id>/<int:price>/', views.send_request , name = 'request' ),
    path('verify/' , views.verify , name = 'verify' ),
    path('eamiltest/' , views.TestEmail.as_view() , name = 'email')

]