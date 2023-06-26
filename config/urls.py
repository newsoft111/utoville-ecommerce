from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include       #new

urlpatterns = [
	path('', include('main.urls')),
	path('', include('account.urls')),
	path('', include('product.urls')),
	path('', include('cart.urls')),
	path('', include('order.urls')),
	path('', include('charge.urls')),
	path('', include('qna.urls')),
	path('', include('revenue.urls')),
	path('', include('profit.urls')),
	path('', include('subscribe.urls')),
	path('', include('house_check.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)