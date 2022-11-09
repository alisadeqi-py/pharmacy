from django.contrib import admin
from django.urls import include, path


urlpatterns = [
path('api/v1/' , include('course.api.v1.urls'))
    
]