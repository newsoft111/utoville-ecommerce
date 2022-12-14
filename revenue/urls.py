from django.urls import path, include
from . import views

app_name = 'revenue'

urlpatterns = [
    path(f'seller/{app_name}/',
		include([
            path('', views.seller_revenue_list, name='seller_revenue_list'),
            path('export/', views.seller_revenue_export, name='seller_revenue_export'),
        ])
    ),
    path(f'admin/{app_name}/',
		include([
            path('', views.admin_revenue_list, name='admin_revenue_list'),
	        path('export/', views.admin_revenue_export, name='admin_revenue_export'),
        ])
    )
]