from django.shortcuts import render, redirect, resolve_url
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
from django.conf import settings
from util.views import EmailSender
User = get_user_model()

def user_login(request):
	seo = {
		'title': "로그인 - 유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		return HttpResponseRedirect(resolve_url('main:index'))
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user = auth.authenticate(request, username=username, password=password)

		if user is not None:
			if user.mb_status == 'Y':
				if user.mb_active == 'Y':
					auth.login(request, user)
					result = '200'
					result_text = '로그인 성공'
				else:
					result = '201'
					result_text = '탈퇴한 계정입니다.'	
			else:
				result = '201'
				result_text = f"관리자에게 문의바랍니다."
		else:
			result = '201'
			result_text = '아이디와 비밀번호를 정확히 입력해 주세요.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)
	else:
		return render(request, 'account/login.html',{"seo":seo})


def user_logout(request):
	auth.logout(request)
	return HttpResponseRedirect(resolve_url('main:index'))


def user_join(request):
	seo = {
		'title': "회원가입 - 유토빌",
	}
	if request.user.is_authenticated:
		return HttpResponseRedirect(resolve_url('main:index'))
	if request.method == 'POST':
		email=request.POST.get('email')
		nickname=request.POST.get('nickname')
		password=request.POST.get('password')
		password2=request.POST.get('password2')

		try:
			_email = User.objects.get(email=email)
		except:
			_email = None
		try:
			_nickname = User.objects.get(nickname=nickname)
		except:
			_nickname = None

		if _email is None:
			if _nickname is None:
				if password == password2:
					user = User.objects.create_user(
																		email=email,
																		nickname=nickname,
																		password=password,
																	)

					
					if send_auth_mail(email):
						result = '200'
						result_text = "회원가입이 완료되었습니다.<br>가입하신 이메일 주소로 인증 메일을 보내드렸습니다.<br>이메일 인증을 한 후에 정상적인 서비스 이용이 가능합니다."
					else:
						result = '201'
						result_text = '알수없는 오류입니다.<br>다시시도 해주세요.'
				else:
					result = '201'
					result_text = '비밀번호가 일치하지 않습니다.'
			else:
				result = '201'
				result_text = '입력한 닉네임은 이미 사용 중입니다.'
		else:
			result = '201'
			result_text = '입력한 이메일은 이미 사용 중입니다.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)

	else:
		return render(request, 'account/join.html', {"seo":seo})


def join_confirm(request, uidb64, token):
	try:
			uid = force_str(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None

	if user is not None:
		if account_activation_token.check_token(user, token):
			user.is_verify = True
			user.save()
			auth.login(request, user)
			message = "인증이 완료되었습니다."
		else:
			message = "이미 인증을 완료했습니다."
	else:
		message = "알수없는 오류입니다. 다시시도 해주세요."
	return render(request, 'main/index.html', {"message":message})


def re_verify(request):
	if request.user.is_authenticated:
		HttpResponseRedirect(resolve_url('main:index'))
	if request.method == 'POST':
		email=request.POST.get('email')

		try:
			_email = User.objects.get(email=email, is_verify=False)
		except:
			_email = None

		if _email is not None and send_auth_mail(email):
			result = '200'
			result_text = f"{email}로 인증 메일을 보내드렸습니다.<br>이메일 인증을 한 후에 정상적인 서비스 이용이 가능합니다."
		else:
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'
		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)

	else:
		return render(request, 'account/re_verify.html')


def find_passwd(request):
	seo = {
		'title': "비밀번호 재설정 - 유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		HttpResponseRedirect(resolve_url('main:index'))
	if request.method == 'POST':
		email = request.POST.get('email')
		try:
			user = User.objects.get(email = email)
		except:
			user = None

		if user is not None:
			emailContent = render_to_string('email/reset_passd.html',{
					'user': user,
					'domain': settings.CURRENT_URL,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': PasswordResetTokenGenerator().make_token(user),
			})

			_result = EmailSender(
				email              = email,
				subject = '[유토빌] 비밀번호 재설정 안내 메일입니다.',
				message = emailContent,
				mailType = 'html'
			)
			
			if _result:
				result = '200'
				result_text = '비밀번호 재설정 메일이 전송되었습니다.<br>메일함을 확인해주세요.'
			else:
				result = '201'
				result_text = '알수없는 오류입니다. 다시시도 해주세요.'
		else:
			result = '201'
			result_text = '등록되지 않은 이메일 입니다.'
		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)   
	else:
		return render(request, 'account/find_passwd.html', {"seo":seo})



def reset_passwd(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None:
		if PasswordResetTokenGenerator().check_token(user, token):
			if request.method == 'POST':
				new_password = request.POST.get("password")
				password_confirm = request.POST.get("password2")
				if new_password == password_confirm:
					user.set_password(new_password)
					user.save()
					result = '200'
					result_text = '비밀번호 변경이 완료되었습니다.<br>변경하신 비밀번호로 다시 로그인 해주시기 바랍니다.'
				else:
					result = '201'
					result_text = '입력하신 비밀번호가 동일하지 않습니다.'

				result = {'result': result, 'result_text': result_text}
				return JsonResponse(result)
			else:
				return render(request, 'account/reset_passwd.html')
		else:
			return render(request, 'main/index.html', {"message":"이미 사용된 인증메일 입니다."})
	else:
		return render(request, 'main/index.html', {"message":"알수없는 오류입니다. 다시시도 해주세요."})



def send_auth_mail(email):
	try:
		user = User.objects.get(email=email)
	except:
		user = None
	
	if user is not None:
		message = render_to_string('email/auth_email.html', {
			'user': user,
			'domain': settings.CURRENT_URL,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			'token': account_activation_token.make_token(user),
		})

		EmailSender(
			email              = email,
			subject = '[유토빌] 이메일 주소 인증을 완료해 주세요.',
			message = message,
			mailType = 'html'
		)
		return True
	else:
		return False


def my_order(request):
	return render(request, 'account/mypage/my_order.html')