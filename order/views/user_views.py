from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ..models import *
from charge.models import *
from django.db.models import Q
import json

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
				'result_text': '로그인을 해주세요.'
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
				variant_value_id = item["variant_value_id"]
			except:
				variant_value_id = None
			ordered_quantity = order_item['qty']


			schedule_date = order_item['schedule_date']
			
			schedule_date.replace(' ', '')

			if schedule_date is None or schedule_date == '':
				return JsonResponse({
					'result': '201', 
					'result_text': '배송날짜 입력바람.'
				})
			
			try:
				product_obj = Product.objects.get(pk=product_id)
				
			except Exception as e:
				return JsonResponse({
					'result': '201', 
					'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
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
						order_item_status = '결제대기',
					)
					total_price += order_item_obj.sub_total_price()

				except Exception as e:
					pass


		order_obj.total_price = total_price
		order_obj.save()
			
		return JsonResponse({
			'result': '200', 
			'result_text': order_obj.pk
		})
	else:
		return redirect("main:index")

