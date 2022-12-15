from .models import *
from product.models import *
from django.db.models import Q


def admin_counter_new_qna(request):
	q = Q()
	q &= Q(answered_at=None)
	result = QnA.objects.filter(q).count()
	return {'admin_counter_new_qna':  result}


def seller_counter_new_qna(request):
	if request.user.is_authenticated:
		q = Q()
		q &= Q(product__user = request.user)
		q &= Q(answered_at = None)
		result = ProductQnA.objects.filter(q).count()
	else:
		result = None
	print(result)
	return {'seller_counter_new_qna':  result}