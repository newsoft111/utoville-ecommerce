from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
	path('user/cart/',
		include([
			path('', views.user_cart_detail, name='user_cart_detail'),
			path('add/', views.user_cart_add_item, name='user_cart_add_item'),
			path('remove/', views.user_cart_remove_item, name='user_cart_remove_item'),
			path('update/', views.user_cart_update, name='user_cart_update'),
		])
	)
]