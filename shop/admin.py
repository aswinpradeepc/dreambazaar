from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ItemsForSale)
admin.site.register(Order)
admin.site.register(CartItem)
