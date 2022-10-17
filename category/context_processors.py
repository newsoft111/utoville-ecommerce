from .models import *
from django.db.models import Q
from collections import defaultdict

def categories(request):
	category_first_list =  CategoryFirst.objects.all().order_by( "id")

	return {
		"category_first_list":category_first_list,

	}