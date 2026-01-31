from rest_framework import serializers
from rest_framework.response import Response
from .models import Product,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','description']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=['id','name','description','price','stock','image','category','created_at','updated_at','is_active']

    category=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
        )
    category=CategorySerializer(read_only=True)
    
