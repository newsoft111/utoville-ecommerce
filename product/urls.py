### users/urls.py
from django.urls import path        #new
from .views import *


urlpatterns = [        #new
    path('', product_list, name="list"),
    path('1/', product_detail, name="detail"),
]