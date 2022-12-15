from .models import *
from django.db.models import Q


def seller_counter_new_order(request):
	if request.user.is_authenticated:
		q = Q()
		q &= Q(is_responded=False)
		q &= Q(product__user = request.user)
		q &= Q(order__payment__is_paid = True)
		result = OrderItem.objects.filter(q).count()
	else:
		result = None
	return {'seller_counter_new_order':  result}