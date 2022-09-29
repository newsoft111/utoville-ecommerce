from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.
def product_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}

	return render(request, 'shop/product_list.html' ,{
		"seo":seo,
	})


class ProductLV(ListView):
	model = Product

