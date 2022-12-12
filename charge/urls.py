from django.urls import path, include
from . import views

app_name = 'charge'

urlpatterns = [
	path('user/charge/',
		include([
			path('', views.payment, name='payment'),
			path('call_back', views.call_back, name='call_back'),
		])
	)
]