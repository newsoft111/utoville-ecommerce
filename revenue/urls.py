from django.urls import path, include
from . import views

app_name = 'revenue'

urlpatterns = [
    path('seller/revenue/',
		include([
            path('', views.seller_revenue_list, name='seller_revenue_list'),
            path('export/', views.seller_revenue_export, name='seller_revenue_export'),
        ])
    ),
    path('admin/revenue/',
		include([
            path('', views.revenue_list, name='list'),
	        path('export/', views.revenue_export, name='export'),
        ])
    )
]