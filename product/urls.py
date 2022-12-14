### users/urls.py
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
	path(f'{app_name}/',
		include([
			path('', views.user_product_list, name="user_product_list"),
			path('<int:product_id>/', views.user_product_detail, name="user_product_detail"),
			path('qna/answer/', views.user_product_qna_question, name="user_product_qna_question"),
			path('review/write/', views.user_product_review_write, name="user_product_review_write"),
		])
	),
	path(f'admin/{app_name}/',
		include([
			path('', views.admin_product_list, name='admin_product_list'),
			path('write/', views.admin_product_write, name='admin_product_write'),
			path('<int:product_id>/', views.admin_product_update, name='admin_product_update'),
			path('delete/', views.admin_product_delete, name='admin_product_delete'),
			path('upload/image', views.admin_product_upload_content_image, name='admin_product_upload_content_image'),
		])
	)
]