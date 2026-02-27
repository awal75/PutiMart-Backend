from django.db.models import post_save
from django.dispatch import receiver
from .models import ProductImage
import os

@receiver(post_save,sender=ProductImage)
def delete_exist_product_image(sender,instance,created,**kwags):
    if created:
        if 