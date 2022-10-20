### users/urls.py
from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
	path('', product_list, name="list"),
	path('<int:product_id>/', product_detail, name="detail"),
	path('qna/answer/', product_qna_answer, name="qna_answer"),
]