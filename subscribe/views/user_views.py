from django.shortcuts import render

# Create your views here.

def user_subscription_about(request):
	return render(request, 'user/subscribe/subscription_about.html')

def user_subscription_book_now(request):
	return render(request, 'user/subscribe/subscription_book_now.html')
	
def user_subscription_check_list_view(request):
	return render(request, 'user/subscribe/subscription_check_list_view.html')