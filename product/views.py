from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
from category.models import *
from collections import defaultdict
import json


# Create your views here.
def product_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}

	category_first_list =  CategoryFirst.objects.all().order_by( "id")

	q = Q()
	if request.GET.get("category1"):
		q &= Q(parent = int(request.GET.get("category1")))
		category_second_list =  CategorySecond.objects.filter(q).order_by( "id")
	else:
		category_second_list = None



	q = Q()
	if request.GET.get("category1"): #카테고리1 필터
		q &= Q(category_first = int(request.GET.get("category1")))
	if request.GET.get("category2"): #카테고리2 필터
		q &= Q(category_second = int(request.GET.get("category2")))
	if request.GET.get("category3"): #카테고리3 필터
		q &= Q(category_third = int(request.GET.get("category3")))
	if request.GET.get("area"): #지역 필터
		q &= Q(productarea__area = request.GET.get("area"))
	if request.GET.get("keyword"): #검색 필터
		q &= Q(name__icontains = request.GET.get("keyword"))

	product_list =  Product.objects.filter(q).order_by( "-id")

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(product_list, 12)
	product_list = pagenator.get_page(page)

	return render(request, 'product/product_list.html' ,{
		"seo":seo,
		"category_first_list":category_first_list,
		"category_second_list":category_second_list,
		"product_list":product_list,
	})


def product_detail(request, product_id):
	seo = {
		'title': "상품 디테일 - 유토빌",
	}

	product_detail = get_object_or_404(Product, pk=product_id)

	q = Q()
	q &= Q(product = product_id)

	variant_list = ProductVariant.objects.filter(q).values_list('id', flat=True).order_by( "-id")
	
	variant_value_list = ProductVariantValue.objects.filter(variant__in=variant_list)

	variant_data = defaultdict(list)
	for variant_value in variant_value_list:
		key = variant_value.variant.variant
		
		tmp_dict = {}
		tmp_dict['value'] = variant_value.value
		tmp_dict['price'] = variant_value.price

		variant_data[key].append(tmp_dict)

	return render(request, 'product/product_detail.html' ,{
		"seo":seo,
		"product_detail": product_detail,
		'variant_data': json.dumps(variant_data)
	})
