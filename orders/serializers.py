from rest_framework import serializers
from .models import Order,OrderItem
from cart.serializers import SimpleProductSerializer
from cart.models import Cart,CartItem
from .service import OrderService



class SimpleItem(serializers.ModelSerializer):
    product=SimpleProductSerializer(read_only=True)
    class Meta:
        model=OrderItem
        fields=['id','price','quantity','total_price','product']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError('Cart does not exist.')

        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Cart is empty.')

        return cart_id

    def create(self, validated_data):
        cart_id = validated_data['cart_id']
        user = self.context['request'].user
        try:
         order=OrderService().create_order(user_id=user,cart_id=cart_id)
         return order 
        except ValueError as e:
            raise serializers.ValidationError(e)
        
    def to_representation(self, instance):
        return OrderSerializer(instance).data
    
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['status']
    
class OrderSerializer(serializers.ModelSerializer):
    orderitems=SimpleItem(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','user','status','total_price','created_at','updated_at','orderitems']
        read_only_fields=['id','user']

    