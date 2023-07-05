from django.shortcuts import render
from product.models import *
from django.db.models import Q
from django.http import JsonResponse
from order.views import create_order

# Create your views here.

def user_subscription_about(request):
	return render(request, 'user/subscribe/subscription_about.html')

def user_subscription_book_now(request):
	return render(request, 'user/subscribe/subscription_book_now.html')
	
def user_subscription_check_list_view(request):
	seo = {
		'title': "Product List - Utoville",
	}

	if request.method == 'POST':
		cleaning_type = request.GET.get("cleaning_type")
		airconditioner_qcy = request.GET.get("airconditioner_qcy")
		bathroom_qcy = request.GET.get("bathroom_qcy")
		bed_qcy = request.GET.get("bed_qcy")
		hood_qcy = request.GET.get("hood_qcy")
		grease_trap_qcy = request.GET.get("grease_trap_qcy")

		order_item_list = [
			{
				"product_id":'66',
				'variant_value_id':'89',
				"qty":airconditioner_qcy,
				"schedule_date":""
			}
		]

		return JsonResponse(
			create_order(request.user, order_item_list)
        )

	else:
		cleaning_checking_id = '66'

		return render(request, 'user/subscribe/subscription_check_list_view.html',{
			"seo":seo,
			"cleaning_checking_id":cleaning_checking_id,
		})