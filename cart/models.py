from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.
User=get_user_model()
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartitems')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartitems')
    quantity=models.PositiveIntegerField(default=0)
