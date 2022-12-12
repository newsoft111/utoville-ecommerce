from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
	path('user/',
		include([
			path('', views.user_index, name='user_index'),
			path('contact/', views.contact, name='contact'),
			path('faq/', views.faq, name='faq'),
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