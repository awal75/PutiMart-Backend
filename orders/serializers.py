from rest_framework import serializers
from .models import Order,OrderItem
from cart.serializers import SimpleProductSerializer
from cart.models import Cart,CartItem
from django.db import transaction
from django.db.models import F, Sum


class SimpleItem(serializers.ModelSerializer):
    product=SimpleProductSerializer(read_only=True)
    class Meta:
        model=OrderItem
        fields=['id','price','quantity','total_price','product']

class CreateOrderSerializer(serializers.Serializer):
    cart_id=serializers.UUIDField()

    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError('This cart is not exits')
        
        if not CartItem.objects.filter(cart=cart_id).exists():
            raise serializers.ValidationError('This cart have no items')
        return cart_id
    
    def create(self, validated_data):
        cart=Cart.objects.get(validated_data['cart_id'])
        user_id=self.context['user_id']

        cart_items=cart.select_relaed('product').annoted(total_price=F('product__price')*F('quantity')).sum('total_price')

        return 
    
class OrderSerializer(serializers.ModelSerializer):
    orderitems=SimpleItem(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','user','status','total_price','created_at','updated_at','orderitems']
        read_only_fields=['id','user']

    