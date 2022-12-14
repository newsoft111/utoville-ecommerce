from django.urls import path, include
from . import views

app_name = 'charge'

user_urlpatterns = [
	path(f'{app_name}/',
		include([
			
			path('', views.user_payment, name='user_payment'),
		])
	)
]

urlpatterns = [
	path(f'{app_name}/call_back/', views.call_back, name='call_back'),
]
urlpatterns += user_urlpatterns