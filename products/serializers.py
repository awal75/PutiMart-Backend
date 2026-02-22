from rest_framework import serializers
from rest_framework.response import Response
from .models import Product,Category,Review
from decimal import Decimal
from django.contrib.auth import get_user_model
User=get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    product_count=serializers.IntegerField(read_only=True)
    class Meta:
        model=Category
        fields=['id','name','description','product_count']


class ProductSerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
        )
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


    
