from django.shortcuts import render
from .models import *
from order.models import *
from django.http import JsonResponse
# Create your views here.

def payment_create(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			'result': '201', 
			'result_text': '로그인을 해주세요.'
		})

	order_id = request.POST.get('order_id')
	used_point = request.POST.get('used_point')

	try:
		order_obj = Order.objects.get(pk=order_id)
	except:
		return JsonResponse({
			'result': '201', 
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		})

	payment_obj = Payment.objects.create()
	payment_obj.used_point = used_point
	payment_obj.save()

	order_obj.payment = payment_obj
	order_obj.save()
		
	return JsonResponse({
		'result': '200', 
		'result_text': payment_obj.pk
	})

