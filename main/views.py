from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	seo = {
		'title': "유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		return redirect('account:my_dashboard')
	else:
		return render(request, 'main/index.html',{"seo":seo})

def contact(request):
	return render(request, 'main/contact.html')

def faq(request):
	return render(request, 'main/faq.html')
