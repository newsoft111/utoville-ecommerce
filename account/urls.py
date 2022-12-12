from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
	path('user/account/',
		include([
			path('login/', views.user_login, name='login'),
			path('logout/', views.user_logout, name='logout'),
			#path('join/', views.user_join, name='join'),
			#path('confirm/<str:uidb64>/<str:token>/', views.join_confirm, name="confirm"),
			#path('find/password/', views.find_passwd, name='find_passwd'),
			#path('reset/password/<str:uidb64>/<str:token>/', views.reset_passwd, name='reset_passwd'),
			#path('re/verify/email/', views.re_verify, name='re_verify'),
			path('mypage/',
				include([
					path('', views.my_dashboard, name='my_dashboard'),
					path('orders/', views.my_order, name='my_order'),
					path('subs/',
						include([
							path('', views.my_subscribe, name='my_subscribe'),
							path('cancel/', views.my_subscribe_cancel, name='my_subscribe_cancel'),			
						]),
					),
					path('qna/',
						include([
							path('', views.qna_list, name='my_qna_list'),
							path('write/', views.qna_write, name='my_qna_write'),
							path('<int:qna_id>/', views.qna_detail, name='my_qna_detail'),
						])
					),
				])
			)
		])
	),
	
	path('seller/account/',
		include([
			path('login/', views.seller_login, name='seller_login'),
			path('logout/', views.seller_logout, name='seller_logout'),
			#path('join/', views.user_join, name='join'),
			#path('confirm/<str:uidb64>/<str:token>/', views.join_confirm, name="confirm"),
			#path('find/password/', views.find_passwd, name='find_passwd'),
			#path('reset/password/<str:uidb64>/<str:token>/', views.reset_passwd, name='reset_passwd'),
			#path('re/verify/email/', views.re_verify, name='re_verify'),
			path('mypage/',
				include([
					path('', views.seller_my_profile, name='seller_my_profile'),
				])
			)
		])
	),

	path('admin/account/',
		include([
			path('', views.account_list, name='list'),
			path('delete/', views.account_delete, name='delete'),
			path('login/', views.user_login, name='login'),
			path('logout/', views.user_logout, name='logout'),
		])
	),
]