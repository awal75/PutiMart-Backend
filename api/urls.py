from django .urls import path,include
from products import views
from rest_framework.routers import SimpleRouter,DefaultRouter

router=DefaultRouter()
router.register('products',views.ProductsModelViewSet,basename='products')
router.register('categories',views.CategoryModelViewSet,basename='categories')

urlpatterns = [
    # # path('products',include('products.products_urls')),
    # path('products/',views.ProductsModelViewSet.as_view({'get': 'list'})),
    # # path('categories',include('products.categories_urls')),
    # path('categories/',views.CategoryModelViewSet.as_view({'get': 'list'})),
    # path('carts',include('cart.urls'))
    path('',include(router.urls))
]
