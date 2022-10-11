from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
from category.models import *
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
	if request.GET.get("category1"):
		q &= Q(category_first = int(request.GET.get("category1")))
	if request.GET.get("category2"):
		q &= Q(category_second = int(request.GET.get("category2")))
	if request.GET.get("category3"):
		q &= Q(category_third = int(request.GET.get("category3")))
	if request.GET.get("area"):
		q &= Q(productarea__area = request.GET.get("area"))

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


   return render(request, 'product/product_detail.html' ,{
      "seo":seo,
      "product_detail": product_detail,
   })