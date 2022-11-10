from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phonenumber = models.CharField(max_length=11,validators=[RegexValidator(r'09(1[0-9]|3[0-9]|2[0-9])-?[0-9]{3}-?[0-9]{4}')])
    address = models.CharField(max_length=500) 
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['phonenumber' , 'address' , 'city' , 'zip_code']
    
    def __str__(self):
        return str(self.username)
    
