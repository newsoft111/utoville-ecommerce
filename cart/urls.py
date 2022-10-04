from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
	path('', views.cart_list, name='list'),
]