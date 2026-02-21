from rest_framework.viewsets import ModelViewSet
from .models import Order,OrderItem
from .serializers import OrderSerializer,SimpleItem,CreateOrderSerializer
from rest_framework import permissions

class OrderModelViewSet(ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['get','post','patch','delete']

    def get_serializer_class(self):
       if self.request.method=='POST':
          return CreateOrderSerializer  
       return OrderSerializer
    
    def get_context_data(self, **kwargs):
        return {'request':self.request}
    

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