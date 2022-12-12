from django.urls import path, include
from . import views

app_name = 'revenue'

urlpatterns = [
    path('seller/revenue/',
		include([
            path('', views.revenue_list, name='list'),
            path('export/', views.revenue_export, name='export'),
        ])
    ),
    path('admin/revenue/',
		include([
            path('', views.revenue_list, name='list'),
	        path('export/', views.revenue_export, name='export'),
        ])
    )
]