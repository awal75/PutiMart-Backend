from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from uuid import uuid4

# Create your models here.
User=get_user_model()
class Cart(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid4)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.first_name}"



class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartitems')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartitems')
    quantity=models.PositiveIntegerField(default=1)

    class Meta:
        unique_together=['cart','product']

    def __str__(self):
        return self.product.name