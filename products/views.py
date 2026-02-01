from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework import status


@api_view(['GET','POST'])
def api_categories(request):
    if request.method=='GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE','PATCH'])
def view_specific_category(request,pk):
    category=get_object_or_404(Category,pk=pk)

    if request.method=='GET':
        # category_dic={'id':category.id,'name':category.name,'description':category.description}
        serializer=CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serializer=CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='PATCH':
        serializer=CategorySerializer(category,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        category.delete()
        return Response({"detail": "Category deleted successfully."},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def api_products(request):
    if request.method=='GET':
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        print(serializer.data[1])
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE','PATCH'])
def view_specific_product(request,pk):

    product=get_object_or_404(Product,pk=pk)
    
    if request.method=='GET':
        # product_dict={'id':product.id,'name':product.name,'price':product.price,'category':{'id':product.category.id,'name':product.category.name}}
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='PATCH':
        serializer=ProductSerializer(product,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        product.delete()
        return Response({"detail": "Category deleted successfully."},status=status.HTTP_204_NO_CONTENT)