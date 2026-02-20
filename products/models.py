from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator,MinValueValidator

User=get_user_model()

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='product_image/',blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    description=models.TextField()
    rating=models.PositiveSmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'user']
        ordering=['-created_at']
