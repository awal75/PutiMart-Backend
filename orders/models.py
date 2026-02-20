from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from uuid import uuid4
User=get_user_model()
# Create your models here.

class Order(models.Model):
    CHOICES=[
        ('not paid','Not Paid'),
        ('ready to ship','Ready To Ship'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('canceled','Canceled')
    ]
    id=models.UUIDField(primary_key=True,editable=False,default=uuid4)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    status=models.CharField(max_length=25,choices=CHOICES,default='not paid')
    total_price=models.DecimalField(max_digits=12,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.first_name} - {self.status}'



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderitems')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orderitems')
    quantity=models.PositiveIntegerField(default=0)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    total_price=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
