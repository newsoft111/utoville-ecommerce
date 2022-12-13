from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
	path('user/',
		include([
			path('', views.user_index, name='user_index'),
			path('contact/', views.user_contact, name='user_contact'),
			path('faq/', views.user_faq, name='user_faq'),
		])
	),
	path('seller/',
		include([
			path('', views.seller_index, name='seller_index'),
		])
	),
	path('admin/',
		include([
			path('', views.admin_index, name='admin_index'),
		])
	)
]