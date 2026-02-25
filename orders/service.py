from cart.models import Cart,CartItem
from django.db.models import F,Sum
from django.db import transaction
from .models import Order,OrderItem
from rest_framework.exceptions import PermissionDenied,ValidationError


class OrderService:

    @staticmethod
    def create_order(user_id,cart_id):
        with transaction.atomic():
            cart = Cart.objects.select_for_update().get(id=cart_id)

            cart_items = CartItem.objects.select_related('product').filter(cart=cart)

            total_price = cart_items.aggregate(
                total=Sum(F('product__price') * F('quantity'))
            )['total']
            print(total_price)
        
            order = Order.objects.create(
                user=user_id,
                total_price=total_price
            )

            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                    total_price=item.product.price * item.quantity,
                )
                for item in cart_items
            ]

            OrderItem.objects.bulk_create(order_items)

            cart.cartitems.all().delete()
            return order
        
    @staticmethod
    def cancel_order(order,user):
        if user.is_staff:
            order.status='canceled'
            order.save()
            return order
        
        if order.user != user :
            raise PermissionDenied({'detail':'You can cancel only your own order'})
        
        if order.status == 'delivered':
            raise ValidationError({'detail':'Your order already delivered so can not cancel at this time'})

        order.status='canceled'
        order.save()
        return order
    
 