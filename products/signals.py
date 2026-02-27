from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import ProductImage
import os


# Image Update hle file delete
@receiver(pre_save, sender=ProductImage)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return  # new object hle kichu  delete hbe nah

    try:
        old_instance = ProductImage.objects.get(pk=instance.pk)
    except ProductImage.DoesNotExist:
        return

    old_file = old_instance.image
    if old_file :
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


#  Object delete hle file delete
@receiver(post_delete, sender=ProductImage)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)