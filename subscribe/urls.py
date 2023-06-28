from django.urls import path, include
from . import views

app_name = 'subscribe'

user_urlpatterns = [
    path(f'{app_name}/',
		include([
			path('about/', views.user_subscription_about, name='user_subscription_about'),
			path('check_list/', views.user_subscription_check_list_view, name='user_subscription_check_list_view'),
        ])
    ),
]

seller_urlpatterns = [
    path(f'seller/{app_name}/',
		include([
            
        ])
    ),
]

admin_urlpatterns = [
    path(f'admin/{app_name}/',
		include([

        ])
    )
]


urlpatterns = user_urlpatterns + seller_urlpatterns + admin_urlpatterns