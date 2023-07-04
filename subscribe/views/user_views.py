from django.shortcuts import render
from product.models import *
from django.db.models import Q
from django.core import serializers

# Create your views here.

def user_subscription_about(request):
	return render(request, 'user/subscribe/about.html')

def user_subscription_check_list_view(request):
	seo = {
		'title': "Product List - Utoville",
	}

	if request.method == 'POST':
		pass
	else:
		q = Q()
		q &= Q(id = "1")

		product_objs =  Product.objects.filter(q).order_by("-id")

		post_list = serializers.serialize('json', product_objs, use_natural_foreign_keys=True)

		return render(request, 'user/subscribe/subscription_check_list_view.html',{
			"seo":seo,
			"product_objs":product_objs,
		})