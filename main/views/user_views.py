from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_index(request):
	seo = {
		'title': "Utoville",
	}

	test_list = [
		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		},

		{
			"review_content" : "리뷰가 들어갈 자리입니다.",
			"review_name" : "이름",
			"review_residence" : "거주지",
			"review_date" : "작성일"
		}
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
