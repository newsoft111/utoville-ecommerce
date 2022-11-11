from django.shortcuts import render
from .models import *
from order.models import *
from django.http import JsonResponse
from revenue.views import Revenue
from profit.views import Profit
# Create your views here.

def call_back(request):
	#이거 그대로 쓰면 안되고 pg사 커스텀 데이터에 order_item_id 리스트 로 넘긴후 Revenue 에 넘겨줘야함
	order_item_id =  OrderItem.objects.filter(order=1).values_list('id', flat=True).order_by( "-id")
	Revenue(order_item_id, 'payment').new_data()
	Profit(order_item_id).new_data()

	return JsonResponse({
		'result': '200', 
		'result_text': '성공'
	})


def payment(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			'result': '201', 
			'result_text': '로그인을 해주세요.'
		})

	order_id = request.POST.get('order_id')
	used_point = request.POST.get('used_point')

	try:
		order_obj = Order.objects.get(pk=order_id)

		payment_obj = Payment.objects.create()

		order_obj.used_point = used_point
		order_obj.payment = payment_obj
		order_obj.save()
	except:
		return JsonResponse({
			'result': '201', 
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		})

	return JsonResponse({
		'result': '200', 
		'result_text': payment_obj.pk
	})

