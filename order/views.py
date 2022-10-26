from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.db.models import Q
import json

@login_required(login_url="account:login")
def order_view(request):
	order_id = request.GET.get("id")
	if order_id is None:
		return redirect('main:index')

	q = Q()
	q &= Q(order=order_id)
	q &= Q(order__user=request.user)
	order_items = OrderItem.objects.filter(q).order_by("-pk")

	total_price=0
	
	for order_item in order_items:
		if order_item.variant_value is not None:
			total_price += (order_item.product_price + order_item.variant_price ) * order_item.ordered_quantity
		else:
			total_price += order_item.product_price * order_item.ordered_quantity

	return render(request, 'order/order_view.html' ,{
		"order_items": order_items,
		"total_price": total_price
	})

def order_create(request):
	if request.method == 'POST':
		if not request.user.is_authenticated:
			return JsonResponse({
				'result': '201', 
				'result_text': '로그인을 해주세요.'
			})

		jsonData = json.loads(request.body)
		order_item_list = json.loads(jsonData.get('order_item_list'))

		order_obj = Order.objects.create(user=request.user)

		for order_item in order_item_list:
			product = order_item['product_id']
			variant_value = order_item['variant_value_id']
			ordered_quantity = order_item['qty']

			try:
				product_obj = Product.objects.get(pk=product)
			except:
				product_obj = None

			try:
				variant_value_obj = ProductVariantValue.objects.get(pk=variant_value)
			except:
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
					OrderItem.objects.create(
						order = order_obj,
						product = product_obj,
						product_name = product_obj.name,
						product_price = product_obj.price,
						variant = variant,
						variant_value = variant_value,
						variant_price = variant_price,
						ordered_quantity = ordered_quantity,
						schedule_date = datetime.now()
						
					)

				except Exception as e:
					print(e)
					pass
			
		return JsonResponse({
			'result': '200', 
			'result_text': order_obj.pk
		})
	else:
		return redirect("main:index")

