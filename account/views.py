from django.shortcuts import render, redirect, resolve_url
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
User = get_user_model()

def user_login(request):
	seo = {
		'title': "로그인 - 유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	if request.method == 'POST':
		email=request.POST.get('email')
		password=request.POST.gaet('password')

		user = auth.authenticate(request, email=email, password=password)

		if user is not None:
			if user.is_verify:
				if user.is_active:
					auth.login(request, user)
					result = '200'
					result_text = '로그인 성공'
				else:
					result = '201'
					result_text = '탈퇴한 계정입니다.'	
			else:
				verify_email_url = resolve_url('VerifyEmail')
				result = '201'
				result_text = f"이메일 인증을 완료해주세요.<a href='{verify_email_url}' class='w-100 btn btn-primary mt-3'>인증메일 다시받기</a>"
		else:
			result = '201'
			result_text = '아이디와 비밀번호를 정확히 입력해 주세요.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)
	else:
		return render(request, 'account/login.html',{"seo":seo})


def user_logout(request):
	auth.logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_join(request):
	seo = {
		'title': "회원가입 - 콘디",
	}
	if request.user.is_authenticated:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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
					result = '200'
					result_text = "성공"
					
					'''if send_auth_mail(email):
						result = '200'
						result_text = "회원가입이 완료되었습니다.<br>가입하신 이메일 주소로 인증 메일을 보내드렸습니다.<br>이메일 인증을 한 후에 정상적인 서비스 이용이 가능합니다."
						AddUserPointLog(user, '회원가입 축하 포인트', 5000)
						MessageSender(user, f"콘디 회원이 되셨습니다.",resolve_url("CampaignWrite"))
					else:
						result = '201'
						result_text = '알수없는 오류입니다.<br>다시시도 해주세요.'''
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