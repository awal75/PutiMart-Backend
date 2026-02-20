from rest_framework import serializers
from .models import Order,OrderItem
from cart.serializers import SimpleProductSerializer
from cart.models import Cart,CartItem


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
    
class OrderSerializer(serializers.ModelSerializer):
    orderitems=SimpleItem(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','user','status','total_price','created_at','updated_at','orderitems']
        read_only_fields=['id','user']

    