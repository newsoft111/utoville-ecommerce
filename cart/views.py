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



def add_cart(request):
	cart = get_user_cart(request)

	product_id=request.POST.get('product_id')

	product = Product.objects.get(pk=product_id)
	quantity = int(request.POST.get('qty')) or 1

	cart_item = CartItem(product=product, cart=cart, quantity=0)
	cart_item.quantity += quantity
	cart_item.save()

	if request.session.get('cart_count'):
		request.session['cart_count'] += quantity
	else:
		request.session['cart_count'] = quantity

	result = '200'
	result_text = '장바구니 넣었음.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)
	


def cart_detail(request, total=0, counter=0, cart_items=None):
	seo = {
		'title': "장바구니 - 유토빌",
	}

	try:
		cart_items = CartItem.objects.filter(cart=get_user_cart(request), active=True)
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


