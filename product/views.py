from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def product_list(request):
<<<<<<< Updated upstream
   seo = {
      'title': "상품 리스트 - 유토빌",
   }
=======
	seo = {
		'title': "상품 리스트 - 유토빌",
	}

	category_list =  CategoryFirst.objects.all().order_by( "-id")
>>>>>>> Stashed changes

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


def product_detail(request, product_id):
   seo = {
      'title': "상품 디테일 - 유토빌",
   }

   product_detail = get_object_or_404(Product, pk=product_id)


   return render(request, 'product/product_detail.html' ,{
      "seo":seo,
      "product_detail": product_detail,
   })