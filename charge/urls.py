from django.urls import path, include
from . import views

app_name = 'charge'

user_urlpatterns = [
	path(f'{app_name}/',
		include([
			path('', views.UserOrderPay.as_view(), name='user_pay'),
		])
	)
]

urlpatterns = [
	path(f'{app_name}/call_back/', views.call_back, name='call_back'),
]
urlpatterns += user_urlpatterns