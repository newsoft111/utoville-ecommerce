from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	#path('join/', views.user_join, name='join'),
	#path('confirm/<str:uidb64>/<str:token>/', views.join_confirm, name="confirm"),
	#path('find/password/', views.find_passwd, name='find_passwd'),
	#path('reset/password/<str:uidb64>/<str:token>/', views.reset_passwd, name='reset_passwd'),
	#path('re/verify/email/', views.re_verify, name='re_verify'),
	path('mypage/',
		include([
			path('orders/', views.my_order, name='my_order'),
			path('subs/', views.subscription, name='subscription'),
			path('cancel/', views.cancel, name='cancel'),
		])
	)
]