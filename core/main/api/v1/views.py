from django.shortcuts import render
from rest_framework.generics import ListAPIView
from Product.models import Product
from ...models import Banner
from .serializers import MainProductSerializer , BannerSerializer




class Banner(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class ProductSpecial(ListAPIView):
    serializer_class = MainProductSerializer
    queryset = Product.objects.filter(status = True , special = True)