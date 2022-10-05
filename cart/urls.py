from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
	path('', views.cart_detail, name='detail'),
	path('add/', views.add_cart, name='add'),
]