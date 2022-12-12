### users/urls.py
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
	path('user/product/',
		include([
			path('', views.product_list, name="list"),
			path('<int:product_id>/', views.product_detail, name="detail"),
			path('qna/answer/', views.product_qna_question, name="qna_question"),
			path('review/write/', views.product_review_write, name="review_write"),
		])
	),
	path('admin/product/',
		include([
			path('', views.product_list, name='list'),
			path('write/', views.product_write, name='write'),
			path('<int:product_id>/', views.product_update, name='update'),
			path('delete/', views.product_delete, name='delete'),
			path('upload/image', views.product_upload_content_image, name='upload_image'),
		])
	)
]