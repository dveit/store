from django.urls import path
from products.views import products, cart_add, cart_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('cart-add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart-delete/<int:id>/', cart_delete, name='cart_delete'),
]
