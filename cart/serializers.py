from rest_framework import serializers
from .models import Cart,CartItem







class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['id','cart','product','quantity']


class CartSerializer(serializers.ModelSerializer):
    cartitems=CartItemSerializer(many=True)

    class Meta:
        model=Cart
        fields=['id','user','created_at','cartitems']

    
