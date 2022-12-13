### users/urls.py
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
	path('user/product/',
		include([
			path('', views.user_product_list, name="user_product_list"),
			path('<int:product_id>/', views.user_product_detail, name="user_product_detail"),
			path('qna/answer/', views.user_product_qna_question, name="user_product_qna_question"),
			path('review/write/', views.user_product_review_write, name="user_product_review_write"),
		])
	),
	path('admin/product/',
		include([
			path('', views.admin_product_list, name='admin_product_list'),
			path('write/', views.product_write, name='write'),
			path('<int:product_id>/', views.product_update, name='update'),
			path('delete/', views.product_delete, name='delete'),
			path('upload/image', views.product_upload_content_image, name='upload_image'),
		])
	)
]