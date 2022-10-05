from django.shortcuts import render
from product.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart


def add_cart(request):
	product_id=request.POST.get('product_id')
	product = Product.objects.get(id=product_id)
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
			cart_id = _cart_id(request)
		)
		cart.save()

	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)
		cart_item.quantity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
			product = product,
			quantity = 1,
			cart = cart
		)
		cart_item.save()

	result = '200'
	result_text = '장바구니 넣었음.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)


def cart_detail(request, total=0, counter=0, cart_items=None):
	seo = {
		'title': "장바구니 - 유토빌",
	}

	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, active=True)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			counter += cart_item.quantity
	except ObjectDoesNotExist:
		pass


	return render(request, 'cart/cart_detail.html' ,
		dict(
			seo = seo,
			cart_items = cart_items,
			total = total,
			counter = counter
		)
	)