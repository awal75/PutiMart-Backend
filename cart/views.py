from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer
from .models import Cart,CartItem
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated



# @api_view(['POST'])
# def view_cart(request):
#     # if request.method=='GET':
#     #     carts=Cart.objects.all()
#     #     serializer=CartSerializer(carts)
#     #     return Response(serializer.data,status=status.HTTP_200_OK)

#     if request.method=='POST':
#         serializer=CartSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class CartModelViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]
    

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_context_data(self, **kwargs):
    #     return {'user':self.request.user }
    
    def get_queryset(self):
        
        return Cart.objects.filter(user=self.request.user)
        
    
    def create(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(
            user=request.user
        )
        serializer = self.get_serializer(cart)

        if created:
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=200)
    

class CartItemModelView(ModelViewSet):
    http_method_names=['get','post','patch','delete']
    permission_classes=[IsAuthenticated]
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_pk':self.kwargs.get('cart_pk'),'request':self.request}
    
    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart=self.kwargs['cart_pk']) 
    
     

    

# @api_view(['GET','DELETE'])
# def view_specific_cart(request,pk):

#     cart=get_object_or_404(Cart,pk=pk)

#     if request.method=='GET':
#         serializer=CartSerializer(cart)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='DELETE':
#         cart.delete()
#         return Response({"message": "cart deleted successfully."},status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET','POST'])
# def view_items(request,cart_id):
#     if request.method== 'GET':
#         cart_items=CartItem.objects.filter(cart=cart_id)
#         serializer=CartItemSerializer(cart_items,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='POST':
#         serializer=CartItemSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

       
   

# @api_view(['GET','PATCH','DELETE'])
# def view_specific_items(request,cart_id,item_id):

#     item=get_object_or_404(CartItem,pk=item_id)
    
#     if request.method=='GET':
#         serializer=CartItemSerializer(item)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     if request.method=='PATCH':
        
#         serializer=CartItemSerializer(item,data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='DELETE':
#         item.delete()
#         return Response({'message':'cartItem deleted successfully.'},status=status.HTTP_204_NO_CONTENT)

   




