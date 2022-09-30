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

<<<<<<< Updated upstream
=======
	product_detail = get_object_or_404(Product, pk=product_id)

	return render(request, 'product/product_detail.html' ,{
		"seo":seo,
		"product_detail": product_detail,
	})
>>>>>>> Stashed changes
