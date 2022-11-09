from django.contrib import admin
from django.urls import include, path

from .views import CourseList , CourseDetail , CourseList , RegisterCourse



urlpatterns = [
    path('form/<int:id>', RegisterCourse.as_view() , name='Course-list') , 
    path('list/', CourseList.as_view() , name='Course-list') , 
    path('<pk>/' , CourseDetail.as_view() , name = 'Course-detail') , 
    
]

# 