from django .urls import path,include
from products import views
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

router=DefaultRouter()
router.register('products',views.ProductsModelViewSet,basename='products')
router.register('categories',views.CategoryModelViewSet,basename='categories')

categories_router=NestedDefaultRouter(router,r'categories',lookup='category')
categories_router.register(r'products',views.ProductsModelViewSet,basename='category-products')

urlpatterns = [
    # # path('products',include('products.products_urls')),
    # path('products/',views.ProductsModelViewSet.as_view({'get': 'list'})),
    # # path('categories',include('products.categories_urls')),
    # path('categories/',views.CategoryModelViewSet.as_view({'get': 'list'})),
    # path('carts',include('cart.urls'))
    path('',include(router.urls)),
    path('',include(categories_router.urls))
]
