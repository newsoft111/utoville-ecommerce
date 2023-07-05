from .models import *
from django.db.models import Q
from collections import defaultdict

def categories(request):
	category_first_list =  CategoryFirst.objects.filter(is_display=True).order_by( "id")

	q = Q()
	if request.GET.get("category1"):
		q &= Q(parent = int(request.GET.get("category1")))
		category_second_list =  CategorySecond.objects.filter(q).order_by( "id")
	else:
		category_second_list = None

	return {
		"category_first_list":category_first_list,
		"category_second_list":category_second_list,
	}