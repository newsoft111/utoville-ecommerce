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
		#cleaning_type 가 basic cleaning 일땐
		#airconditioner_qcy, bathroom_qcy, bed_qcy, hood_qcy, grease_trap_qcy

		#cleaning_type 가 whole cleaning 일땐
		#아직 작업안함

		q = Q()
		q &= Q(variant_id__product_id='66')

		if request.GET.get("cleaning_type") == 'basic_cleaning':
			q &= Q(variant_id='43')
		else:
			q &= Q(variant_id='44')

		variant_value_objs = ProductVariantValue.objects.filter()


		order_item_list = []

		for variant_value_obj in variant_value_objs:
			variant_value = str(variant_value_obj.value).lower().replace(" ", "_")
			qty = request.GET.get(f"{variant_value}_qcy")

			order_item = {
				"product_id": '66',
				"variant_value_id": variant_value_obj.id,
				"qty": qty,
				"schedule_date": ""
			}
			order_item_list.append(order_item)

		return JsonResponse(
			create_order(request.user, order_item_list)
        )

	else:
		cleaning_checking_id = '66'

		return render(request, 'user/subscribe/subscription_check_list_view.html',{
			"seo":seo,
			"cleaning_checking_id":cleaning_checking_id,
		})