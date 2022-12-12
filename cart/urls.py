from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
	path('user/cart/',
		include([
			path('', views.cart_detail, name='detail'),
			path('add/', views.add_cart, name='add'),
			path('remove/', views.remove_cart, name='remove'),
			path('update/', views.update_cart, name='update'),
		])
	)
]