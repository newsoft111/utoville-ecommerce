from django.urls import path, include
from . import views

app_name = 'house_check'

user_urlpatterns = [
    path(f'{app_name}/',
		include([
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