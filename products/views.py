from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from .serializers import ProductSerializer
from rest_framework import status

@api_view()
def view_specific_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category_dic={'id':category.id,'name':category.name,'description':category.description}
    return Response(category_dic)

@api_view()
def api_products(request):
    product=Product.objects.all()
    serializer=ProductSerializer(product,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view()
def view_specific_product(request,pk):

    product=get_object_or_404(Product,pk=pk)
    product_dict={'id':product.id,'name':product.name,'price':product.price,'category':{'id':product.category.id,'name':product.category.name}}
    return Response(product_dict)