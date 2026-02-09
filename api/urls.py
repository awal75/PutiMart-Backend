from django .urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from products import views
from cart.views import CartModelViewSet,CartItemModelView

router=DefaultRouter()
router.register(r'products',views.ProductsModelViewSet,basename='products')
router.register(r'categories',views.CategoryModelViewSet,basename='categories')
router.register(r'reviews',views.ReviewModelViewSet,basename='reviews')
router.register(r'carts',CartModelViewSet,basename='carts')
router.register(r'items',CartItemModelView,basename='items')

categories_router=NestedDefaultRouter(router,r'categories',lookup='category')
categories_router.register(r'products',views.ProductsModelViewSet,basename='category-products')
preoducts_review_router=NestedDefaultRouter(router,r'products',lookup='product')
preoducts_review_router.register(r'reviews',views.ReviewModelViewSet,basename='product-reviews')

carts_router=NestedDefaultRouter(router,r'carts',lookup='cart')
carts_router.register(r'items',CartItemModelView,basename='cart-items')


urlpatterns = [
    # # path('products',include('products.products_urls')),
    # path('products/',views.ProductsModelViewSet.as_view({'get': 'list'})),
    # # path('categories',include('products.categories_urls')),
    # path('categories/',views.CategoryModelViewSet.as_view({'get': 'list'})),
    # path('carts',include('cart.urls'))
    path('',include(router.urls)),
    path('',include(categories_router.urls)),
    path('',include(preoducts_review_router.urls)),
    path('',include(carts_router.urls))

]
