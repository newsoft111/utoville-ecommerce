from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
	path('user/order/',
		include([
			path('', views.order_view, name='view'),
			path('create/', views.order_create, name='create'),
		])
	),
	path('seller/order/',
		include([
			path('', views.seller_order_list, name='seller_order_list'),
			path('preview/', views.OrderPreview.as_view(), name='preview'),
			path('edit/status/', views.order_edit_status, name='edit_status'),
		])
	),
	path('admin/order/',
		include([
			path('', views.order_list, name='list'),
		])
	)
]