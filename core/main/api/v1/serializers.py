from Product.models import Product
from rest_framework import serializers
from ...models import Banner 

class MainProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            'name',
            'category',
            'image',
            'price',
            'special',
        ]

class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner

        fields = [
            'Product',
            'Banner',
        ]