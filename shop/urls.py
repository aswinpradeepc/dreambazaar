from django.urls import path
from shop.views import *

urlpatterns = [
    path('shop-grid', shop_grid_view),
    # Dynamic url for individual pdt
    path('shop-details/<int:id>', shop_details_view, name='shop-details'),
    path('shopping-cart', shopping_cart_view),
    path('checkout', checkout_view),
    path('categories/<str:cat>', department_view, name='categories'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
]
