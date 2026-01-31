from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category

@api_view()
def view_specific_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category_dic={'id':category.id,'name':category.name,'description':category.description}
    return Response(category_dic)

@api_view()
def view_specific_product(request,pk):

    product=get_object_or_404(Product,pk=pk)
    product_dict={'id':product.id,'name':product.name,'price':product.price,'category':{'id':product.category.id,'name':product.category.name}}
    return Response(product_dict)