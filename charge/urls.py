from django.urls import path, include
from . import views

app_name = 'charge'

urlpatterns = [
	path('charge/',
		include([
			path('call_back', views.call_back, name='call_back'),
		])
	),
	path('user/charge/',
		include([
			path('', views.user_payment, name='user_payment'),
		])
	)
]