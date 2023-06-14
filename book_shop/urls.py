from django.urls import path
from book_shop.views import *

urlpatterns = [
    path('shop-grid', shop_grid_view),
    path('shop-details', shop_details_view),
]