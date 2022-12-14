from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
	path(f'{app_name}/',
		include([
			path('login/', views.user_login, name='user_login'),
			path('logout/', views.user_logout, name='user_logout'),
			#path('join/', views.user_join, name='join'),
			#path('confirm/<str:uidb64>/<str:token>/', views.join_confirm, name="confirm"),
			#path('find/password/', views.find_passwd, name='find_passwd'),
			#path('reset/password/<str:uidb64>/<str:token>/', views.reset_passwd, name='reset_passwd'),
			#path('re/verify/email/', views.re_verify, name='re_verify'),
			path('mypage/',
				include([
					path('', views.user_my_dashboard, name='user_my_dashboard'),
					path('orders/', views.user_my_order, name='user_my_order'),
					path('subs/',
						include([
							path('', views.user_my_subscribe, name='user_my_subscribe'),
							path('cancel/', views.user_my_subscribe_cancel, name='user_my_subscribe_cancel'),			
						]),
					),
					path('qna/',
						include([
							path('', views.user_my_qna_list, name='user_my_qna_list'),
							path('write/', views.user_my_qna_write, name='user_my_qna_write'),
							path('<int:qna_id>/', views.user_my_qna_detail, name='user_my_qna_detail'),
						])
					),
				])
			)
		])
	),
	
	path(f'seller/{app_name}/',
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

	path(f'admin/{app_name}/',
		include([
			path('', views.admin_account_manage_list, name='admin_account_manage_list'),
			path('delete/', views.admin_account_manage_delete, name='admin_account_manage_delete'),
			path('login/', views.admin_login, name='admin_login'),
			path('logout/', views.admin_logout, name='admin_logout'),
		])
	),
]