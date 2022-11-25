from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
	path('', views.order_view, name='view'),
	path('create/', views.order_create, name='create'),
	path('chart/done/', views.get_order_done, name='chart_done'),
]