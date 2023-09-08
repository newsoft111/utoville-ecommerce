from django.urls import path, include
from . import views

app_name = 'profit'

seller_urlpatterns = [
    path(f'seller/{app_name}/',
		include([
            path('', views.seller_profit_list, name='seller_profit_list'),
            path('preview/', views.SellerProfitPreview.as_view(), name='seller_profit_preview'),
            path('export/', views.seller_profit_export, name='seller_profit_export'),
        ])
    ),
]

admin_urlpatterns = [
	path(f'admin/{app_name}/',
		include([
			path('', views.admin_profit_list, name='admin_profit_list'),
			path('<int:profit_id>/', views.admin_profit_detail, name='admin_profit_detail'),
			path('change/status/', views.admin_profit_change_status, name='admin_profit_change_status'),
			path('change/memo/', views.admin_profit_change_memo, name='admin_profit_change_memo'),
        ])
    )
]

urlpatterns = seller_urlpatterns + admin_urlpatterns