from django.urls import path, include
from . import views

app_name = 'qna'

user_urlpatterns = [
    path(f'{app_name}/',
		include([
        ])
    ),
]

seller_urlpatterns = [
    path(f'seller/{app_name}/',
		include([
            path('', views.seller_qna_list, name='seller_qna_list'),
            path('<int:qna_id>/', views.seller_qna_detail, name='seller_qna_detail'),
            path('delete/', views.seller_qna_delete, name='seller_qna_delete'),
        ])
    ),
]

admin_urlpatterns = [
    path(f'admin/{app_name}/',
		include([
            path('', views.admin_qna_list, name='admin_qna_list'),
			path('<int:qna_id>/', views.admin_qna_detail, name='admin_qna_detail'),
        ])
    )
]


urlpatterns = user_urlpatterns + seller_urlpatterns + admin_urlpatterns