from django.urls import path
from . import views

urlpatterns=[
    # path('',views.api_products,name='products-list'),
    path('',views.ViewProducts.as_view()),
    # path('/<int:pk>',views.view_specific_product),
    path('/<int:pk>',views.ViewProduct.as_view())

]