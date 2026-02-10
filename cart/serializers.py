from rest_framework import serializers
from .models import Cart,CartItem
from products.models import Product





class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']


class CartItemSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer()
    total_price=serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model=CartItem
        fields=['id','product','quantity','total_price']

    def get_total_price(self,cartItem: CartItem):
        return cartItem.quantity*cartItem.product.price


class CartSerializer(serializers.ModelSerializer):
    cartitems=CartItemSerializer(many=True)
    total_price=serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model=Cart
        fields=['id','user','total_price','created_at','cartitems']

    def get_total_price(self,cart: Cart):
        return sum([item.product.price * item.quantity for item in cart.cartitems.all()])

    
