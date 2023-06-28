from django.shortcuts import render

# Create your views here.

def user_subscription_about(request):
	return render(request, 'user/subscribe/about.html')

def user_subscription_check_list_view(request):
	return render(request, 'user/subscribe/subscription_check_list_view.html')