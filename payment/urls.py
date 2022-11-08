from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
	#path('', views.order_view, name='view'),
	path('create/', views.payment_create, name='create'),
]