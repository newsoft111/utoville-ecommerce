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
            path('', views.qna_list, name='list'),
            path('<int:qna_id>/', views.qna_detail, name='detail'),
            path('delete/', views.qna_delete, name='delete'),
        ])
    ),
    path('admin/qna/',
		include([
            path('', views.qna_list, name='list'),
			path('<int:qna_id>/', views.qna_detail, name='detail'),
        ])
    )
]