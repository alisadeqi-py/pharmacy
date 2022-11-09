from django.contrib import admin
from .models import Course , CourseCategory , RegisteredUser

# Register your models here.


admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(RegisteredUser)
