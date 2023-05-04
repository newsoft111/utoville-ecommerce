from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..tokens import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta, date
from django.conf import settings
from util.views import EmailSender
from order.models import *
from qna.models import *
from django.core.paginator import Paginator
from django.db.models import Q, Count, F
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
import json
User = get_user_model()

def user_login(request):
	seo = {
		'title': "Login - Utoville",
	}
	if request.user.is_authenticated: #로그인 상태면
		return HttpResponseRedirect(resolve_url('main:user_index'))
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user = auth.authenticate(request, username=username, password=password)

		if user is None:
			result = '201'
			result_text = 'Please enter your ID and password correctly.'
			return JsonResponse({'result': result, 'result_text': result_text})

		if user.mb_status != 'Y':
			result = '201'
			result_text = "Please contact the administrator."
			return JsonResponse({'result': result, 'result_text': result_text})

		if user.mb_active == 'Y':
			auth.login(request, user)
			result = '200'
			result_text = 'Welcome to Utoville Homecare.'
		else:
			result = '201'
			result_text = 'This account has been terminated.'	

		return JsonResponse({'result': result, 'result_text': result_text})
	else:
		return render(request, 'user/account/login.html',{"seo":seo})


def user_logout(request):
	auth.logout(request)
	return HttpResponseRedirect(resolve_url('main:user_index'))


def user_join(request):
	seo = {
		'title': "Join - Utoville",
	}
	if request.user.is_authenticated:
		return HttpResponseRedirect(resolve_url('main:user_index'))
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

		if _email is not None:
			result = '201'
			result_text = 'This email is already in use.'
			return JsonResponse({'result': result, 'result_text': result_text})

		if _nickname is not None:
			result = '201'
			result_text = 'This nickname is already in use.'
			return JsonResponse({'result': result, 'result_text': result_text})

		if password != password2:
			result = '201'
			result_text = 'The passwords do not match.'
			return JsonResponse({'result': result, 'result_text': result_text})
		

		user = User.objects.create_user(
								email=email,
								nickname=nickname,
								password=password,
							)
		
		if send_auth_mail(email):
			result = '200'
			result_text = 'Your registration has been completed.<br>We have sent a confirmation email to the email address you provided.<br>Please verify your email address to access our services.'
		else:
			result = '201'
			result_text = 'An unknown error has occurred.<br>Please try again.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)

	else:
		return render(request, 'user/account/join.html', {"seo":seo})


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
			message = "Authentication has been completed."
		else:
			message = "Authentication has already been completed."
	else:
		message = "An unknown error has occurred.<br>Please try again."
	return render(request, 'user/main/index.html', {"message":message})


def re_verify(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(resolve_url('main:user_index'))
	if request.method == 'POST':
		email=request.POST.get('email')

		try:
			_email = User.objects.get(email=email, is_verify=False)
		except:
			_email = None

		if _email is not None and send_auth_mail(email):
			result = '200'
			result_text = f"We have sent a confirmation email to {email}. <br>Please verify your email address to access our services."
		else:
			result = '201'
			result_text = 'An unknown error has occurred.<br>Please try again.'
		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)

	else:
		return render(request, 'user/account/re_verify.html')


def find_passwd(request):
	seo = {
		'title': "Password reset - Utoville",
	}
	if request.user.is_authenticated: #로그인 상태면
		return HttpResponseRedirect(resolve_url('main:user_index'))
	if request.method == 'POST':
		email = request.POST.get('email')
		try:
			user = User.objects.get(email = email)
		except:
			user = None

		if user is None:
			result = '201'
			result_text = 'This email is not registered.'
			return JsonResponse({'result': result, 'result_text': result_text})


		emailContent = render_to_string('email/reset_passd.html',{
				'user': user,
				'domain': settings.CURRENT_URL,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': PasswordResetTokenGenerator().make_token(user),
		})

		_result = EmailSender(
			email   = email,
			subject = '[Utoville] This is an e-mail informing you of resetting your password.',
			message = emailContent,
			mailType = 'html'
		)
		
		if _result:
			result = '200'
			result_text = 'A password reset email has been sent. <br>Please check your mailbox.'
		else:
			result = '201'
			result_text = 'An unknown error has occurred.<br>Please try again.'
			
		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)   
	else:
		return render(request, 'user/account/find_passwd.html', {"seo":seo})



def reset_passwd(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is None:
		return render(request, 'user/main/index.html', {"message":"An unknown error has occurred.<br>Please try again."})
		
	if not PasswordResetTokenGenerator().check_token(user, token):
		return render(request, 'user/main/index.html', {"message":"This confirmation email has already been used."})


	if request.method == 'POST':
		new_password = request.POST.get("password")
		password_confirm = request.POST.get("password2")
		if new_password == password_confirm:
			user.set_password(new_password)
			user.save()
			result = '200'
			result_text = 'Your password has been successfully changed. <br>Please log in again with your new password.'
		else:
			result = '201'
			result_text = 'The passwords you entered do not match.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)
	else:
		return render(request, 'user/account/reset_passwd.html')


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
			subject = '[Utoville] Please complete your email address verification.',
			message = message,
			mailType = 'html'
		)
		return True
	else:
		return False

@login_required(login_url="account:user_login")
def user_my_dashboard(request):
	"""Here we are preparing data to show order detail on user's calender"""
	
	if request.user.is_authenticated and not request.user.is_anonymous:
		order_data = []

		q = Q()
		q &= Q(order__user=request.user)

		order_items = OrderItem.objects.filter(q)
		for items in order_items:
			item_data = {'title': items.product_name, 'start': str(items.schedule_date), 'className': 'bg-success'
			if items.is_delivered else 'bg-info'}
			order_data.append(item_data)

	q = Q()
	q &= Q(order__user=request.user)
	try:
		next_service_day_count = OrderItem.objects.filter(q).order_by('-schedule_date')[0].schedule_date
		next_service_day_count = (next_service_day_count.replace(tzinfo=None) - (datetime.today() - timedelta(1))).days

		if next_service_day_count < 1:
			next_service_day_count = 0
	except:
		next_service_day_count = 0
		
	q &= Q(is_delivered=True)
	delivered_service_count = OrderItem.objects.filter(q).count()

	water_derivery_category = CategoryFirst.objects.get(name=settings.WATER_DELIVERY_SERVICE_NAME)
	q = Q()
	q &= Q(order__user=request.user)
	q &= Q(product__category_first=water_derivery_category.id)
	q &= Q(is_delivered=False)
	
	water_delivered_service_list = OrderItem.objects.values('ordered_quantity', 'shipped_quantity').filter(q)
	water_delivered_service_count = 0
	for water_delivered_service in water_delivered_service_list:
		water_delivered_service_count += water_delivered_service["ordered_quantity"] - water_delivered_service["shipped_quantity"]


	#완료된 서비스 시작
	q = Q()
	q &= Q(order__user = request.user)
	q &= ~Q(order__payment = None)
	q &= Q(is_delivered = True)
	

	order_done_objs =  OrderItem.objects.filter(q).values(name=F('product__category_first__name')).annotate(
		value=Count('pk')
	)
	order_done_data = []
	order_done_keys = []
	for order_done_objs in order_done_objs:
		order_done_keys.append(order_done_objs['name'])
		order_done_data.append({'value': order_done_objs['value'], 'name': order_done_objs['name']})


	#완료된 서비스 끝

	return render(request, 'user/account/mypage/my_dashboard.html', {
		"orders": order_data,
		'delivered_service_count':delivered_service_count,
		"next_service_day_count": next_service_day_count,
		"water_delivered_service_count": water_delivered_service_count,
		"order_done_data": order_done_data,
		"order_done_keys":order_done_keys
	})

@login_required(login_url="account:user_login")
def user_my_order(request):
	seo = {
		'title': "Product list - Utoville",
	}

	order_status_dict = {
		"1":"Payment Awaiting",
		"2":"Payment Completed",
		"3":"Delivery Awaiting",
		"4":"Delivery Completed",
	}

	q = Q()
	q &= Q(order__user = request.user)
	q &= ~Q(order__payment__paid_at = None)

	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	end_date = end_date + timedelta(days=1)

	q &= Q(order__payment__paid_at__range = [start_date, end_date])

	keyword = request.GET.get("keyword")
	if keyword is not None and keyword != '':
		q &= Q(product_name__icontains = keyword)

	category = request.GET.get("category_by")
	if category is not None and category != '':
		q &= Q(product__category_first = category)

	order_item_status = request.GET.get("status_by")
	if order_item_status is not None and order_item_status != '':
		q &= Q(order_item_status = order_status_dict[order_item_status])

	my_order_objs =  OrderItem.objects.filter(q).order_by("-id")
	print(str(my_order_objs.query))

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(my_order_objs, 6)
	my_order_objs = pagenator.get_page(page)

	category_objs = CategoryFirst.objects.all().order_by("id")

	q = Q()
	q &= Q(product__user = request.user)

	return render(request, 'user/account/mypage/my_order.html' ,{
		"seo":seo,
		"my_order_objs":my_order_objs,
		"category_objs": category_objs,
		'order_status_dict': order_status_dict.items(),
	})

@login_required(login_url="account:user_login")
def user_my_subscribe(request):
	return render(request, 'user/account/mypage/my_subscribe.html')

@login_required(login_url="account:user_login")
def user_my_subscribe_cancel(request):
	return render(request, 'user/account/mypage/my_subscribe_cancel.html')

@login_required(login_url="account:user_login")
def user_my_qna_list(request):
	seo = {
		'title': "Product List - Utoville",
	}

	q = Q()
	q &= Q(user = request.user)

	qna_objs =  QnA.objects.filter(q).order_by('-id')

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(qna_objs, 12)
	qna_objs = pagenator.get_page(page)

	return render(request, 'user/account/mypage/my_qna_list.html' ,{
	 	"seo":seo,
	 	"qna_objs":qna_objs,
	})

def user_my_qna_write(request):
	if request.method == 'POST':
		jsonData = json.loads(request.body)
		subject = jsonData.get('subject')
		question = jsonData.get('question')
		qna_type = jsonData.get('question')

		if subject is None or subject == '':
			result = {'result': '201', 'result_text': 'Please enter title.'}
			return JsonResponse(result)

		if question is None or question == '':
			result = {'result': '201', 'result_text': 'Please enter your question.'}
			return JsonResponse(result)

		if qna_type is None or qna_type == '':
			result = {'result': '201', 'result_text': 'Please select a type of question.'}
			return JsonResponse(result)

		try:
			qna_obj = QnA()
			qna_obj.user = request.user
			qna_obj.subject = subject
			qna_obj.question = question
			qna_obj.qna_type = qna_type
			qna_obj.save()

			result = {'result': '200', 'result_text': 'Your question has been registered.'}
			return JsonResponse(result)

		except Exception as e:
			print(e)
			result = {'result': '201', 'result_text': 'An unknown error has occurred. Please contact the administrator.'}
			return JsonResponse(result)
	else:
		return render(request, 'user/account/mypage/my_qna_write.html')

def user_my_qna_detail(request, qna_id):
	seo = {
		'title': "Product List - Utoville",
	}
	
	q = Q()
	q &= Q(user = request.user)
	q &= Q(pk = qna_id)

	qna_obj =  get_object_or_404(QnA, q)
	return render(request, 'user/account/mypage/my_qna_detail.html' ,{
	 	"seo":seo,
	 	"qna_obj":qna_obj,
	})
