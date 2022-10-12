from django.shortcuts import render, redirect
from product.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

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
		cart_items = CartItem.objects.filter(cart=get_user_cart(request), active=True)
		for cart_item in cart_items:
			total_price += (cart_item.product.price + cart_item.variant_value.price ) * cart_item.quantity
			total_quantity += cart_item.quantity
	except ObjectDoesNotExist:
		pass
		
	return {
		"total_price": total_price,
		"total_quantity": total_quantity
	}


def add_cart(request):
	cart = get_user_cart(request)

	product_id = request.POST.get('product_id')

	product = Product.objects.get(pk=product_id)
	quantity = int(request.POST.get('qty')) or 1
	variant_value_id = request.POST.get('variant_value_id')


	try:
		cart_item = CartItem.objects.get(product=product, cart=cart, variant_value=variant_value_id)
		cart_item.quantity += quantity
		cart_item.save()
	except CartItem.DoesNotExist:
		variant_value = ProductVariantValue.objects.get(variant_value=variant_value_id)

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


def remove_cart(request):
	cart = get_user_cart(request)

	cart_item_id=request.POST.get('cart_item_id')

	cart_item = CartItem.objects.get(pk=cart_item_id, cart=cart)
	cart_item.delete()
	
	result = '200'
	result_text = '장바구니 삭제함.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)


def update_cart(request):
	cart = get_user_cart(request)

	cart_item_id=request.POST.get('cart_item_id')
	quantity = int(request.POST.get('qty')) or 1

	cart_item = CartItem.objects.get(pk=cart_item_id, cart=cart)
	cart_item.quantity = quantity
	cart_item.save()

	cart_info = get_cart_info(request)
	total_price = cart_info['total_price']
	total_quantity = cart_info['total_quantity']

	result = '200'
	result_text = '장바구니 업데이트 되었음.'
	custom_data = {
		"total_price": format(total_price, ','),
		"total_quantity": total_quantity
	}

	result = {'result': result, 'result_text': result_text, "custom_data": custom_data}
	return JsonResponse(result)
	


def cart_detail(request, total_price=0, counter=0, cart_items=None):
	seo = {
		'title': "장바구니 - 유토빌",
	}

	try:
		cart_items = CartItem.objects.filter(cart=get_user_cart(request), active=True)
	except ObjectDoesNotExist:
		pass

	cart_info = get_cart_info(request)
	total_price = cart_info['total_price']
	total_quantity = cart_info['total_quantity']

	return render(request, 'cart/cart_detail.html' ,
		dict(
			seo = seo,
			cart_items = cart_items,
			total_price = total_price,
			total_quantity = total_quantity
		)
	)


