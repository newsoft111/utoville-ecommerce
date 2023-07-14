from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_index(request):
	seo = {
		'title': "Utoville",
	}

	test_list = [
		{
			"review_content" : "Communications with Fernanda to set up the date and time were good, both by email and text. The cleaner Danyelle was very thorough! She cleaned both of my bathrooms and the floors of my bedroom, hall, kitchen, dining room and family room. They look great! I will not hesitate to use this service again!",
			"review_name" : "Peggy Jupp",
			"review_residence" : "manilla",
			"review_date" : "2023.07.01"
		},
		
	]

	if request.user.is_authenticated: #로그인 상태면
		return redirect('account:user_my_dashboard')
	else:
		return render(request, 'user/main/index.html',{"seo":seo, "review":test_list})
	
def user_contact(request):
	return render(request, 'user/main/contact.html')

def user_faq(request):
	return render(request, 'user/main/faq.html')

# @login_required(login_url="account:seller_login")
def partnership_inquiry(request):
	return render(request, 'user/main/partnership_inquiry.html')
