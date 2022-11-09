from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('phone_number' , {'fields':('phonenumber',)}) , ('address' , {'fields':('address',)})
)
admin.site.register(User, UserAdmin)


('Additional info', {
        'fields': ('New Field',)
    })