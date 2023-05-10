from django.shortcuts import render
from ..models import *
from order.models import *
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
import json
from charge.dragon import DragonPay
# Create your views here.



class UserOrderPay(View):
	def get(self, request):
		return HttpResponse('404')
	
	def post(self, request):
		if not request.user.is_authenticated:
			return JsonResponse({
				'result': '201', 
				'result_text': 'Need to login.'
			})
			
		jsonData = json.loads(request.body)

		order_id = jsonData.get('order_id')
		used_point = jsonData.get('used_point')

		amount  = jsonData.get('amount')
		description = jsonData.get('description')
		transaction_id = jsonData.get('transaction_id')

		try:
			order_obj = Order.objects.get(pk=order_id)

			payment_obj = Payment.objects.create(user=request.user)

			order_obj.used_point = used_point
			order_obj.payment = payment_obj
			order_obj.save()
			
		except Exception as e:
			return JsonResponse({
				'result': '201', 
				'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
			})

			
		param1 = {
			"order_id" : order_id,
			"user_id" : request.user.id,
			"result_url" : ''
		}
		dragon_pay = DragonPay()
		return JsonResponse(
			{"url":dragon_pay.pay(
				order_obj.txnid,
				amount,
				description,
				request.user.email,
				param1
			)}
		)
