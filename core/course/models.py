from django.db import models
from account.models import User

# Create your models here.



class CourseCategory(models.Model):
    name = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length = 250)
    category = models.ForeignKey(CourseCategory , null= True ,on_delete = models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)
    time = models.IntegerField()
    start_date = models.DateTimeField(auto_now = True)
    create_date = models.DateTimeField(auto_now=True)
    Update_date = models.DateTimeField(auto_now_add =True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class RegisteredUser(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE ) 
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    identification_card = models.ImageField()
    picture = models.ImageField()

    def __str__(self):
        return str(self.user)
