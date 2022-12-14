from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
	path(f'{app_name}/',
		include([
			path('', views.user_order_view, name='user_order_view'),
			path('create/', views.user_order_create, name='user_order_create'),
		])
	),
	path(f'seller/{app_name}/',
		include([
			path('', views.seller_order_list, name='seller_order_list'),
			path('preview/', views.SellerOrderPreview.as_view(), name='seller_order_preview'),
			path('edit/status/', views.seller_order_edit_status, name='seller_order_edit_status'),
		])
	),
	path(f'admin/{app_name}/',
		include([
			path('', views.admin_order_list, name='admin_order_list'),
		])
	)
]