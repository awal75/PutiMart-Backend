from django .urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from products import views
from cart.views import CartModelViewSet,CartItemModelView
from orders.views import OrderModelViewSet,OrderItemModelViewSet

router=DefaultRouter()
router.register(r'products',views.ProductsModelViewSet,basename='products')
router.register(r'categories',views.CategoryModelViewSet,basename='categories')
router.register(r'carts',CartModelViewSet,basename='carts')
router.register(r'orders',OrderModelViewSet,basename='orders')

categories_router=NestedDefaultRouter(router,r'categories',lookup='category')
categories_router.register(r'products',views.ProductsModelViewSet,basename='category-products')
product_image_router=NestedDefaultRouter(router,r'products',lookup='product')
product_image_router.register(r'images',views.ProductImageModelViewSet,basename='product-images')
preoducts_review_router=NestedDefaultRouter(router,r'products',lookup='product')
preoducts_review_router.register(r'reviews',views.ReviewModelViewSet,basename='product-reviews')

carts_router=NestedDefaultRouter(router,r'carts',lookup='cart')
carts_router.register(r'items',CartItemModelView,basename='cart-items')

# order_router=NestedDefaultRouter(router,r'orders',lookup='order')
# order_router.register(r'order-items',OrderItemModelViewSet,basename='order-items')

urlpatterns = [
    # # path('products',include('products.products_urls')),
    # path('products/',views.ProductsModelViewSet.as_view({'get': 'list'})),
    # # path('categories',include('products.categories_urls')),
    # path('categories/',views.CategoryModelViewSet.as_view({'get': 'list'})),
    # path('carts',include('cart.urls'))
    path('',include(router.urls)),
    path('',include(categories_router.urls)),
    path('',include(preoducts_review_router.urls)),
    path('',include(carts_router.urls)),
    path('',include(product_image_router.urls))
    # path('',include(order_router.urls))

]
