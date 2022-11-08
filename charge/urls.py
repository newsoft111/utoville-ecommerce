from django.urls import path, include
from . import views

app_name = 'charge'

urlpatterns = [
	path('', views.payment, name='payment'),
]