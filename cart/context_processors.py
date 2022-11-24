from .models import *
from django.db.models import Q
from .views import get_user_cart
from django.core.exceptions import ObjectDoesNotExist
from .models import *


def counter_cart_items(request):
	try:
		cart_items = CartItem.objects.filter(
			cart=get_user_cart(request),
			product__is_deleted=False
		)
	except ObjectDoesNotExist:
		pass
	return {'counter_cart_items':  cart_items.count()}