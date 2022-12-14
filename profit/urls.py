from django.urls import path, include
from . import views

app_name = 'profit'

urlpatterns = [
    path('seller/profit/',
		include([
            path('', views.seller_profit_list, name='seller_profit_list'),
            path('preview/', views.SellerProfitPreview.as_view(), name='seller_profit_preview'),
            path('export/', views.seller_profit_export, name='seller_profit_export'),
        ])
    ),
	path('admin/profit/',
		include([
            path('', views.admin_profit_list, name='admin_profit_list'),
			path('export/', views.admin_profit_export, name='admin_profit_export'),
			path('catalog/', views.admin_profit_catalog, name='admin_profit_catalog'),
        ])
    )
]