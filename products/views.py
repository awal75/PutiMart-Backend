from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category,Review,ProductImage
from .serializers import ProductSerializer,CategorySerializer,ReviewSerializer,ProductImageSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import DefaultPagination
# from rest_framework import permissions
from api import permissions

class CategoryModelViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(permissions.IsAdminOrReadOnly,)


class ProductsModelViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=ProductFilter
    search_fields=['name','description','category__name']
    ordering_fields=['price','updated_at']
    pagination_class=DefaultPagination
    permission_classes=(permissions.IsAdminOrReadOnly,)

class ProductImageModelViewSet(ModelViewSet):
    serializer_class=ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product=self.kwargs['product_pk'])
    
    def perform_create(self, serializer):
        return serializer.save(product=self.kwargs['product_pk'])
    

class ReviewModelViewSet(ModelViewSet):
    serializer_class=ReviewSerializer
    permission_classes=[permissions.IsAdminOrReadOnly]
    pagination_class=DefaultPagination
    
    def get_queryset(self):
        reviews=Review.objects.all()
        product_pk=self.kwargs.get('product_pk')

        if product_pk:
           reviews= reviews.filter(product=product_pk)
           
        return reviews
    
    def get_serializer_context(self):
        return {
            'product_pk':self.kwargs['product_pk'],
            'request':self.request
                
                }
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




# @api_view(['GET','POST'])
# def api_categories(request):
#     if request.method=='GET':
#         categories=Category.objects.select_related('products').annotate(product_count=Count('products')).all()
        
#         serializer=CategorySerializer(categories,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='POST':
#         serializer=CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#  #use api_view   
# class ViewCategories(APIView):
#     def get(self,request):
#         categories=Category.objects.annotate(product_count=Count('products'))
#         serializer=CategorySerializer(categories,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer=CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


# class CategoriesListCreateAPIView(ListCreateAPIView):
#     queryset=Category.objects.annotate(product_count=Count('products'))
#     serializer_class=CategorySerializer


# @api_view(['GET','PUT','DELETE','PATCH'])
# def view_specific_category(request,pk):
#     category=get_object_or_404(Category,pk=pk)

#     if request.method=='GET':
#         # category_dic={'id':category.id,'name':category.name,'description':category.description}
#         serializer=CategorySerializer(category)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PUT':
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PATCH':
#         serializer=CategorySerializer(category,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class ViewCategory(APIView):
#     def get(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         serializer=CategorySerializer(category)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    

#     def patch(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         serializer=CategorySerializer(category,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    

#     def delete(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class=CategorySerializer
#     queryset=Category.objects.all()
    

# @api_view(['GET','POST'])
# def api_products(request):
#     if request.method=='GET':
#         search=request.GET.get('search')
#         category=request.GET.get('category')
#         print(request.query_params)

#         product=Product.objects.all()

#         if search:
#             product=product.filter(name__icontains=search) # name diye filter krte hbe
#         if category:
#             product=product.filter(category=category)

#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class ViewProducts(APIView):

#     def get(self,request):
#         search=request.query_params.get('search')
#         category=request.query_params.get('category')
    

#         product=Product.objects.all()

#         if search:
#             product=product.filter(name__icontains=search) # name diye filter krte hbe
#         if category:
#             product=product.filter(category=category)

#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
# class ProductsListCeateApiView(ListCreateAPIView):
#     serializer_class=ProductSerializer

#     def get_queryset(self):
#         search=self.request.query_params.get('search')
#         category=self.request.query_params.get('category')
    

#         product=Product.objects.all()

#         if search:
#             product=product.filter(name__icontains=search) # name diye filter krte hbe
#         if category:
#             product=product.filter(category=category)
#         return product
    
        

# @api_view(['GET','PUT','DELETE','PATCH'])
# def view_specific_product(request,pk):

#     product=get_object_or_404(Product,pk=pk)
    
#     if request.method=='GET':
#         # product_dict={'id':product.id,'name':product.name,'price':product.price,'category':{'id':product.category.id,'name':product.category.name}}
#         serializer=ProductSerializer(product)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PUT':
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PATCH':
#         serializer=ProductSerializer(product,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ViewProduct(APIView):

#     def get(self,request,pk):
#         product=get_object_or_404(Product,pk=pk)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         product=get_object_or_404(Product,pk=pk)
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def patch(self,request,pk):
#         product=get_object_or_404(Product,pk=pk)
#         serializer=ProductSerializer(product,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def delete(self,request,pk):
#         product=get_object_or_404(Product,pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class productRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer