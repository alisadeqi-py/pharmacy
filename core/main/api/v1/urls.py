from django.contrib import admin
from django.urls import include, path
from .views import Banner , ProductSpecial



urlpatterns = [
   path('Banner/', Banner.as_view() , name='Banner-list') , 
   path('products/' , ProductSpecial.as_view() , name = 'Product-detail')
    
]