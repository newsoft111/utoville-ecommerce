from django.urls import path, include
from . import views

app_name = 'charge'

urlpatterns = [
	path(f'{app_name}/',
		include([
			path('call_back', views.call_back, name='call_back'),
			path('', views.user_payment, name='user_payment'),
		])
	),
	
]