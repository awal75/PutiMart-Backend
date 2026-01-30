from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
User=get_user_model()
# Create your models here.

class Order(models.Model):
    CHOICES=[
        ('pending','Pending'),
        ('shipped','Shipped'),
        ('delivered','Delivered')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    status=models.CharField(max_length=25,choices=CHOICES,default='pending')
    total_price=models.DecimalField(max_digits=12,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderitems')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orderitems')
    quantity=models.PositiveIntegerField(default=0)
    price=models.DecimalField(max_digits=12,decimal_places=2)
