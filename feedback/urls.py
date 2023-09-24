from django.urls import path
from feedback.views import *

urlpatterns = [
    path('feedback', feedback_view),
]