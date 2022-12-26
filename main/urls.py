from django.urls import path, include
from . import views

app_name = 'main'

user_urlpatterns = [
	path('',
		include([
			path('', views.user_index, name='user_index'),
			path('contact/', views.user_contact, name='user_contact'),
			path('faq/', views.user_faq, name='user_faq'),
			path('regist/', views.business_regist, name='business_regist'),
		])
	)
]

seller_urlpatterns = [
	path('seller/',
		include([
			path('', views.seller_index, name='seller_index'),
		])
	)
]


admin_urlpatterns = [
	path('admin/',
		include([
			path('', views.admin_index, name='admin_index'),
		])
	)
]

urlpatterns = user_urlpatterns + seller_urlpatterns + admin_urlpatterns