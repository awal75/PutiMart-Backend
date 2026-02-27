from rest_framework import serializers
from rest_framework.response import Response
from .models import Product,Category,Review,ProductImage
from decimal import Decimal
from django.contrib.auth import get_user_model
User=get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    product_count=serializers.IntegerField(read_only=True)
    class Meta:
        model=Category
        fields=['id','name','description','product_count']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['id','image']

class ProductSerializer(serializers.ModelSerializer):
   
    price_tax=serializers.SerializerMethodField(
        method_name='get_price_with_tax',
    )
    images=ProductImageSerializer(many=True,read_only=True,source='product_images')
    category=CategorySerializer(read_only=True)

    class Meta:
        model=Product
        fields=['id','name','description','price','price_tax','stock','category','created_at','updated_at','is_active','images']
        

    def get_price_with_tax(self,product):
        return round(product.price*Decimal('1.10'),2)
    



class SimpleUserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(
        method_name='get_User_full_name')
    class Meta:
        model= User
        fields=['id','name']

    def get_User_full_name(self,user):
        return user.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
    user=SimpleUserSerializer(read_only=True)
    class Meta:
        model=Review
        fields=['id','product','user','description','rating','created_at']
        read_only_fields=['product']

    def create(self, validated_data):
        product_pk=self.context['product_pk']
        print(product_pk)
        return Review.objects.create(product_id=product_pk,**validated_data)
    

    def validate(self, attrs):
        product_id = self.context['product_pk']
        user = self.context['request'].user

        if Review.objects.filter(product_id=product_id, user=user).exists():
            raise serializers.ValidationError(
                "You have already reviewed this product."
            )
        return attrs


    
