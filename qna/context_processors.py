from .models import *
from django.db.models import Q


def admin_counter_new_qna(request):
	q = Q()
	q &= Q(answered_at=None)
	result = QnA.objects.filter(q).count()
	return {'admin_counter_new_qna':  result}