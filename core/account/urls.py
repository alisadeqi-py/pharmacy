from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('' ,  include('django.contrib.auth.urls')),
    path('api/v1/' , include('account.api.v1.urls'))
    
]