from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_products,name='products-list'),
    path('/<int:pk>',views.view_specific_product),
    # path('/<int:pk>',views,name='products-show'),
    # path('/<int:pk>',views,name='products-update'),
    # path('/<int:pk>',views,name='products-delete'),
]