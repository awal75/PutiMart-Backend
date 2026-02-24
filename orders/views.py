from rest_framework.viewsets import ModelViewSet
from .models import Order,OrderItem
from .serializers import OrderSerializer,SimpleItem,CreateOrderSerializer,UpdateOrderSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from .service import OrderService
from rest_framework.response import Response

class OrderModelViewSet(ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['get','post','patch','delete','head','options']

    @action(detail=True,methods=['post'],permission_classes=[permissions.IsAuthenticated])
    def cancel(self,request,pk=None):
       order=self.get_object()
       OrderService.cancel_order(order=order,user=self.request.user)
       
       return Response({'detail':'Order canceled'},status=200)
    
    @action(detail=True,methods=['post'],permission_classes=[permissions.IsAdminUser],url_name='update-status')
    def update_status(self,request,pk=None):
       order=self.get_object()
       
    





    def get_serializer_class(self):
         if self.request.method=='POST':
            return CreateOrderSerializer 
         elif self.request.method=='PATCH':
            return UpdateOrderSerializer
         return OrderSerializer
    def get_permissions(self):
       if self.request.method == 'DELETE':
          return [permissions.IsAdminUser()]
       return [permissions.IsAuthenticated()]
    
    def get_serializer_context(self):
         return {'request': self.request}
    

    def get_queryset(self):
     if self.request.user.is_staff:
        return Order.objects.prefetch_related('orderitems','orderitems__product')
     return Order.objects.prefetch_related('orderitems','orderitems__product').filter(user=self.request.user)
    
   #  def perform_create(self, serializer):
   #     serializer.save(user=self.request.user)


class OrderItemModelViewSet(ModelViewSet):
   permission_classes=[permissions.IsAuthenticated]
   serializer_class=SimpleItem
   
   def get_queryset(self):
      order_pk=self.kwargs.get('order_pk')
      return OrderItem.objects.filter(order=order_pk)