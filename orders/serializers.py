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
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError('Cart does not exist.')

        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Cart is empty.')

        return cart_id

    @transaction.atomic
    def create(self, validated_data):
        cart_id = validated_data['cart_id']
        user = self.context['request'].user

        cart = Cart.objects.get(id=cart_id)

        # Get cart items with product in one query
        cart_items = CartItem.objects.select_related('product').filter(cart=cart)

        # Calculate total price
        total_price = cart_items.aggregate(
            total=Sum(F('product__price') * F('quantity'))
        )['total']

        # Create Order
        order = Order.objects.create(
            user=user,
            total_price=total_price
        )


        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_items)

   
        cart.delete()

        return order 
    
class OrderSerializer(serializers.ModelSerializer):
    orderitems=SimpleItem(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','user','status','total_price','created_at','updated_at','orderitems']
        read_only_fields=['id','user']

    