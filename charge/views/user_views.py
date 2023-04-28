from django.shortcuts import render
from ..models import *
from order.models import *
from django.http import JsonResponse
# Create your views here.



def user_payment(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			'result': '201', 
			'result_text': 'Please log in.'
		})

	order_id = request.POST.get('order_id')
	used_point = request.POST.get('used_point')

	try:
		order_obj = Order.objects.get(pk=order_id)

		payment_obj = Payment.objects.create(user=request.user)

		order_obj.used_point = used_point
		order_obj.payment = payment_obj
		order_obj.save()
	except Exception as e:
		print(e)
		return JsonResponse({
			'result': '201', 
			'result_text': 'An unknown error has occurred. Please try again.'
		})

	return JsonResponse({
		'result': '200', 
		'result_text': payment_obj.pk
	})

