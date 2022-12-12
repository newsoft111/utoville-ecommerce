from django.shortcuts import render, redirect, resolve_url
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..tokens import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
from django.conf import settings
from util.views import EmailSender
from django.contrib.auth.decorators import login_required
User = get_user_model()

def seller_login(request):
	
	seo = {
		'title': "로그인 - 유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		return HttpResponseRedirect(resolve_url('main:seller_index'))
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		
		user = auth.authenticate(request, username=username, password=password)

		if user is None:
			result = '201'
			result_text = '아이디와 비밀번호를 정확히 입력해 주세요.'
			return JsonResponse({'result': result, 'result_text': result_text})
		
		if user.mb_status != 'Y':
			result = '201'
			result_text = f"관리자에게 문의바랍니다."
			return JsonResponse({'result': result, 'result_text': result_text})

		if user.mb_active == 'Y':
			auth.login(request, user)
			result = '200'
			result_text = '로그인 성공'
		else:
			result = '201'
			result_text = '탈퇴한 계정입니다.'	
		

		return JsonResponse({'result': result, 'result_text': result_text})
	else:
		return render(request, 'seller/account/login.html',{"seo":seo})


def seller_logout(request):
	auth.logout(request)
	return HttpResponseRedirect(resolve_url('main:seller_index'))



@login_required(login_url="account:login")
def seller_my_profile(request):
	if request.method == 'POST':
		password=request.POST.get('password')
		new_password=str(request.POST.get('new_password')).replace(' ', '')
		new_password2=str(request.POST.get('new_password2')).replace(' ', '')
		mb_name=request.POST.get('mb_name')
		mb_phone=request.POST.get('mb_phone')

		user = auth.authenticate(request, username=request.user.username, password=password)

		if user is None:
			return JsonResponse({
				'result': '201', 
				'result_text': '비밀번호를 정확히 입력해 주세요.'
			})
		
		if user.mb_status != 'Y':

			#auth.logout(request)

			return JsonResponse({
				'result': '201', 
				'result_text': '관리자에게 문의바랍니다.'
			})

		if mb_name is None or mb_name == '':
			return JsonResponse({
				'result': '201', 
				'result_text': '담당자명을 입력해 주세요.'
			})

		if mb_phone is None or mb_phone == '':
			return JsonResponse({
				'result': '201', 
				'result_text': '담당자 연락처을 입력해 주세요.'
			})

		if new_password is not None and new_password != '':
			if new_password != new_password2:
				return JsonResponse({
					'result': '201', 
					'result_text': '변경 비밀번호가 동일하지 않습니다.'
				})


		try:
			user = User.objects.get(pk=request.user.id)
		except(TypeError, ValueError, OverflowError, User.DoesNotExist):
			return JsonResponse({
				'result': '201', 
				'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
			})

		if new_password is not None and new_password != '':
			user.set_password(new_password)
		
		user.mb_name = mb_name
		user.mb_phone = mb_phone
		user.save()

		return JsonResponse({
			'result': '200', 
			'result_text': '변경이 완료되었습니다.'
		})


	else:
		return render(request, 'seller/account/my_profile.html')


