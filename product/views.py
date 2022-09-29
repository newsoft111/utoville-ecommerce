from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def product_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}

	q = Q()
	#q &= Q(is_deleted = True)


	product_list =  Product.objects.filter(q).order_by( "-id")
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(product_list, 12)
	product_list = pagenator.get_page(page)

	return render(request, 'product/product_list.html' ,{
		"seo":seo,
		"product_list":product_list,
	})


def product_detail(request):
	seo = {
		'title': "상품 디테일 - 유토빌",
	}


	return render(request, 'product/product_detail.html' ,{
		"seo":seo,
	})
