from django.urls import path, include
from . import views

app_name = 'profit'

urlpatterns = [
    path('seller/profit/',
		include([
            path('', views.profit_list, name='list'),
            path('preview/', views.ProfitPreview.as_view(), name='preview'),
            path('export/', views.profit_export, name='export'),
            path('catalog', views.profit_catalog, name='catalog'),
        ])
    )
]