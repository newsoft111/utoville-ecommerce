from django.urls import path, include
from . import views

app_name = 'qna'

urlpatterns = [
    path('user/qna/',
		include([
        ])
    ),
    path('seller/qna/',
		include([
            path('', views.seller_qna_list, name='seller_qna_list'),
            path('<int:qna_id>/', views.seller_qna_detail, name='seller_qna_detail'),
            path('delete/', views.seller_qna_delete, name='seller_qna_delete'),
        ])
    ),
    path('admin/qna/',
		include([
            path('', views.qna_list, name='list'),
			path('<int:qna_id>/', views.qna_detail, name='detail'),
        ])
    )
]