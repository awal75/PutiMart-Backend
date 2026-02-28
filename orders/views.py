from rest_framework.viewsets import ModelViewSet
from .models import Order,OrderItem
from .serializers import OrderSerializer,SimpleItem,CreateOrderSerializer,UpdateOrderSerializer,EmptySerializer
from rest_framework import permissions
from rest_framework.decorators import action
from .service import OrderService
from rest_framework.response import Response

class OrderModelViewSet(ModelViewSet):
    http_method_names=['get','post','delete','head','options']

    @action(detail=True,methods=['post'])
    def cancel(self,request,pk=None):
       if getattr(self, 'swagger_fake_view', False):
        return {}
       order=self.get_object()
       OrderService.cancel_order(order=order,user=self.request.user)
       
       return Response({'status':'Order canceled'},status=200)
    
    @action(detail=True,methods=['patch'],url_path='update-status')
    def update_status(self,request,pk=None):
       order=self.get_object()
       serializer=UpdateOrderSerializer(order,data=request.data,partial=True)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data,status=200)

    def get_serializer_class(self):
         if self.action=='create':
            return CreateOrderSerializer 
         elif self.action=='cancel':
            return EmptySerializer
         elif self.action == 'update_status':
            return UpdateOrderSerializer
         return OrderSerializer
    
    def get_permissions(self):
       if self.action in ['destroy','update_status']:
          return [permissions.IsAdminUser()]
       return [permissions.IsAuthenticated()]
    
    def get_serializer_context(self):
         if getattr(self, 'swagger_fake_view', False):
            return {}
         return {'request': self.request}
    

    def get_queryset(self):
     if getattr(self,'swagger_fake_view',False):
      return Order.objects.none()

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