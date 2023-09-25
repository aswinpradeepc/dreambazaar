# search/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('search_items', views.search_items, name='search_items'),
]
