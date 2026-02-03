from rest_framework import serializers
from rest_framework.response import Response
from .models import Product,Category
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','description']


class ProductSerializer(serializers.ModelSerializer):
    # category=serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    #     write_only=True
    #     )
    # category=CategorySerializer(read_only=True)
    # category=serializers.HyperlinkedRelatedField(
    #     view_name='view-specfic-category',
    #     queryset=Category.objects.all()
  
    #  )
    price_tax=serializers.SerializerMethodField(
        method_name='get_price_with_tax',
    )

    class Meta:
        model=Product
        fields=['id','name','description','price','price_tax','stock','image','category','created_at','updated_at','is_active']
        

    def get_price_with_tax(self,product):
        return round(product.price*Decimal('1.10'),2)

    
