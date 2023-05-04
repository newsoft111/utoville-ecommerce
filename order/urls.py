from django.urls import path, include
from . import views

app_name = 'order'


user_urlpatterns = [
	path(f'{app_name}/',
		include([
			path('', views.user_order_view, name='user_order_view'),
			path('pay/', views.user_order_pay, name='user_order_pay'),
			path('create/', views.user_order_create, name='user_order_create'),
		])
	),
]

seller_urlpatterns = [
	path(f'seller/{app_name}/',
		include([
			path('', views.seller_order_list, name='seller_order_list'),
			path('<int:order_item_id>/', views.seller_order_detail, name='seller_order_detail'),
			path('preview/', views.SellerOrderPreview.as_view(), name='seller_order_preview'),
			path('edit/status/', views.seller_order_edit_status, name='seller_order_edit_status'),
		])
	),
]

admin_urlpatterns = [
	path(f'admin/{app_name}/',
		include([
			path('', views.admin_order_list, name='admin_order_list'),
			path('<int:order_item_id>/', views.admin_order_detail, name='admin_order_detail'),
		])
	)
]


urlpatterns = user_urlpatterns + seller_urlpatterns + admin_urlpatterns