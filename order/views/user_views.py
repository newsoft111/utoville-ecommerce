from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from ..models import *
from charge.models import *
from django.db.models import Q
import json
from charge.dragon import DragonPay
import uuid

@login_required(login_url="account:user_login")
def user_order_view(request):
	order_id = request.GET.get("id")
	if order_id is None:
		return redirect('main:index')

	q = Q()
	q &= Q(order=order_id)
	q &= Q(order__user=request.user)
	order_items = OrderItem.objects.filter(q).order_by("-pk")
	
	return render(request, 'user/order/order_view.html' ,{
		"order_items": order_items,

	})


def user_order_create(request):
	if request.method == 'POST':
		if not request.user.is_authenticated:
			return JsonResponse({
				'result': '201', 
				'result_text': 'Please log in.'
			})

		jsonData = json.loads(request.body)
		order_item_list = json.loads(jsonData.get('order_item_list'))

		order_obj = Order.objects.create(
			user=request.user,
			total_price=0,
			used_point=0
		)

		total_price = 0

		for order_item in order_item_list:
			product_id = order_item['product_id']
			try:
				variant_value_id = order_item["variant_value_id"]
			except:
				variant_value_id = None
			ordered_quantity = order_item['qty']


			schedule_date = order_item['schedule_date']
			
			schedule_date.replace(' ', '')

			if schedule_date is None or schedule_date == '':
				return JsonResponse({
					'result': '201', 
					'result_text': 'Please enter the delivery date.'
				})
			
			try:
				product_obj = Product.objects.get(pk=product_id)
				
			except Exception as e:
				return JsonResponse({
					'result': '201', 
					'result_text': 'An unknown error has occurred. Please try again.'
				})

			try:
				variant_value_obj = ProductVariantValue.objects.get(pk=variant_value_id)
			except Exception as e:
				variant_value_obj = None
			
			if variant_value_obj is not None:
				variant = variant_value_obj.variant
				variant_value = variant_value_obj.value
				variant_price = variant_value_obj.price
			else:
				variant = None
				variant_value = None
				variant_price = None


			if product_obj is not None:
				try:
					order_item_obj = OrderItem.objects.create(
						order = order_obj,
						product = product_obj,
						product_name = product_obj.product_name,
						product_price = product_obj.price,
						variant = variant,
						variant_value = variant_value,
						variant_price = variant_price,
						ordered_quantity = ordered_quantity,
						schedule_date = schedule_date,
						order_item_status = 'Payment awaiting',
					)
					total_price += order_item_obj.sub_total_price()

				except Exception as e:
					pass


		order_obj.total_price = total_price
		order_obj.save()
			
		return JsonResponse({
			'result': '200', 
			'order_pk': order_obj.pk,
			'transaction_id' : order_obj.txnid
		})
	else:
		return redirect("main:user_index")



class UserOrderPay(View):
	def get(self, request):
		return HttpResponse('404')
	
	def post(self, request):
		jsonData = json.loads(request.body)
		amount  = jsonData.get('amount')
		description = jsonData.get('description')
		order_pk = jsonData.get('order_pk')
		transaction_id = jsonData.get('transaction_id')
		param1 = {
			"order_pk" : order_pk,
			"user_pk" : request.user.id
		}
		dragon_pay = DragonPay()
		return JsonResponse(
			{"url":dragon_pay.token_pay(
				transaction_id, #txnid
				amount, #금액
				description, #메모
				request.user.email, #이메일
				param1 #부가정보
			)}
		)
