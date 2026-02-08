from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CartSerializer,CartItemSerializer
from .models import Cart,CartItem
from rest_framework.viewsets import ModelViewSet



@api_view(['POST'])
def view_cart(request):
    # if request.method=='GET':
    #     carts=Cart.objects.all()
    #     serializer=CartSerializer(carts)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer=CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class CartModelViewSet(ModelViewSet):
    serializer_class=CartSerializer

    queryset=Cart.objects.all()

class CartItemModelView(ModelViewSet):
    serializer_class=CartItemSerializer

    def get_queryset(self):
        cartItems=CartItem.objects.all()
        cart_id=self.kwargs.get('cart_id')
        if cart_id:
            cartItems=cartItems.filter(cart=cart_id)
        return cartItems

    

@api_view(['GET','DELETE'])
def view_specific_cart(request,pk):

    cart=get_object_or_404(Cart,pk=pk)

    if request.method=='GET':
        serializer=CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        cart.delete()
        return Response({"message": "cart deleted successfully."},status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def view_items(request,cart_id):
    if request.method== 'GET':
        cart_items=CartItem.objects.filter(cart=cart_id)
        serializer=CartItemSerializer(cart_items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

       
   

@api_view(['GET','PATCH','DELETE'])
def view_specific_items(request,cart_id,item_id):

    item=get_object_or_404(CartItem,pk=item_id)
    
    if request.method=='GET':
        serializer=CartItemSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='PATCH':
        
        serializer=CartItemSerializer(item,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        item.delete()
        return Response({'message':'cartItem deleted successfully.'},status=status.HTTP_204_NO_CONTENT)

   




