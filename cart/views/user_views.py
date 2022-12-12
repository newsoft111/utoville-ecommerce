from django.shortcuts import render, redirect
from product.models import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

def get_user_cart(request):
	cart_id = None
	cart = None

	if request.user.is_authenticated and not request.user.is_anonymous:
		try:
			cart = Cart.objects.get(user=request.user)
		except Cart.DoesNotExist:
			cart = Cart(user=request.user)
			cart.save()
	else:
		cart_id = request.session.get('cart_id')
		if not cart_id:
			cart = Cart()
			cart.save()
			request.session['cart_id'] = cart.id
		else:
			cart = Cart.objects.get(id=cart_id)
	return cart


def get_cart_info(request):
	total_price=0
	total_quantity=0

	try:
		cart_items = CartItem.objects.filter(cart=get_user_cart(request))
		for cart_item in cart_items:
			if cart_item.variant_value is not None:
				total_price += (cart_item.product.price + cart_item.variant_value.price ) * cart_item.quantity
			else:
				total_price += cart_item.product.price * cart_item.quantity
			total_quantity += cart_item.quantity
	except ObjectDoesNotExist:
		pass
		
	return {
		"total_price": total_price,
		"total_quantity": total_quantity
	}


def user_cart_add_item(request):
	cart = get_user_cart(request)
	item_list = json.loads(request.POST.get('data'))

	for item in item_list:

		product = Product.objects.get(pk=item["product_id"])
		variant_value_id = item["variant_value_id"] or None
		quantity = int(item["qty"]) or 1
		
		try:
			cart_item = CartItem.objects.get(product=product, cart=cart, variant_value=variant_value_id)
			cart_item.quantity += quantity
			cart_item.save()
		except CartItem.DoesNotExist:
			if variant_value_id is not None:
				variant_value = ProductVariantValue.objects.get(pk=variant_value_id)
			else:
				variant_value = None

			cart_item = CartItem.objects.create(
				product=product, 
				cart=cart,
				variant_value=variant_value,
				quantity=1
			)


	result = '200'
	result_text = '장바구니 넣었음.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)


def user_cart_remove_item(request):
	cart = get_user_cart(request)

	cart_item_id=request.POST.getlist('cart_item_id[]')

	cart_items = CartItem.objects.filter(pk__in=cart_item_id, cart=cart)
	for cart_item in cart_items:
		cart_item.is_deleted = True
		cart_item.deleted_at = datetime.now()
		cart_item.save()
	
	result = '200'
	result_text = '장바구니 삭제함.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)


def user_cart_update(request):
	cart = get_user_cart(request)

	cart_item_id=request.POST.get('cart_item_id')
	print(cart_item_id)
	quantity = int(request.POST.get('qty')) or 1

	try:
		cart_item = CartItem.objects.get(pk=cart_item_id, cart=cart)
		cart_item.quantity = quantity
		cart_item.save()


		result = '200'
		result_text = '업데이트 성공'
	except Exception as e:
		print(e)
		result = '201'
		result_text = '알수없는 오류입니다. 다시시도 해주세요.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)
	

def user_cart_detail(request, total_price=0, counter=0, cart_items=None):
	seo = {
		'title': "장바구니 - 유토빌",
	}

	try:
		cart_items = CartItem.objects.filter(
			cart=get_user_cart(request),
			product__is_deleted=False
		)
	except ObjectDoesNotExist:
		pass

	'''cart_info = get_cart_info(request)
	total_price = cart_info['total_price']
	total_quantity = cart_info['total_quantity']'''

	return render(request, 'user/cart/cart_detail.html' ,
		dict(
			seo = seo,
			cart_items = cart_items,
		)
	)