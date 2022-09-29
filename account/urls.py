from django.urls import path, include
from . import views

urlpatterns = [
	path('login/', views.user_login, name='accounts_login'),
	path('logout/', views.user_logout, name='accounts_logout'),
	path('join/', views.user_join, name='accounts_join'),
]