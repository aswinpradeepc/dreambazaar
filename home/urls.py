from django.contrib import admin
from django.urls import path
from home.views import *
from feedback.views import feedback_view

urlpatterns = [
    path('', home_view),
    path('signup', signup_view),
    path('login', login_view),

]
