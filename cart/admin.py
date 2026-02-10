from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.


# admin.site.register(Cart)
@admin.register(Cart)
class CardAdmin(admin.ModelAdmin):
    list_display=['id','user']

admin.site.register(CartItem)