from django.contrib import admin
from django.urls import path, include       #new

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('main.urls')),
	path('account/', include('account.urls')),
	path('product/', include('product.urls')),
	path('cart/', include('cart.urls')),
	path('order/', include('order.urls')),
	path('charge/', include('charge.urls')),
]