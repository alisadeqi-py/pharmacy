from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from .views import CustomDiscardAuthToken , RegistrationApiView , UserUpdateApiView , ChangePasswordApiView
urlpatterns = [
    #registration 
    path('registration/' , RegistrationApiView.as_view() , name='registration'),
    path('update/' , UserUpdateApiView.as_view() , name='UserUpdate'),
    path('changepass/' , ChangePasswordApiView.as_view() , name = 'reserpassword'),

   
    #auth_token 
    path('token/login/' , views.ObtainAuthToken.as_view() , name='auth_token'),
    path('token/logout/' , CustomDiscardAuthToken.as_view() , name='auth_token'),
    ]
# 