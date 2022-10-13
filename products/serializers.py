from rest_framework import serializers
from .models import Products,Categorey,Brand

class GetProductsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    city =serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    categorey = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Products
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name']


class CategoreySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorey
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
