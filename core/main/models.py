from django.db import models
from Product.models import Product
# Create your models here.


class Banner(models.Model):
    Product = models.ForeignKey(Product , on_delete = models.CASCADE)
    Banner = models.ImageField()




