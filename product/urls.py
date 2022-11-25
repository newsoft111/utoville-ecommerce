### users/urls.py
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
	path('', views.product_list, name="list"),
	path('<int:product_id>/', views.product_detail, name="detail"),
	path('qna/answer/', views.product_qna_question, name="qna_question"),
	path('review/write/', views.product_review_write, name="review_write"),
]