from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from order.models import *
# Create your views here.
@login_required(login_url="account:seller_login")
def seller_index(request):
	seo = {
		'title': "유토빌",
	}

	order_data_calendar = []

	q = Q()
	q &= Q(product__user=request.user)
	q &= Q(order__payment__is_paid = True)

	order_items = OrderItem.objects.filter(q)
	for items in order_items:
		item_data = {'id':items.pk, 'title': items.product_name, 'start': str(items.schedule_date), 'className': 'bg-success'
		if items.order_item_status == '배달완료' else 'bg-danger' if items.order_item_status == '주문취소' else 'bg-info'}
		order_data_calendar.append(item_data)


	return render(request, 'seller/main/index.html',{
		"seo":seo,
		"order_data_calendar": order_data_calendar,
	})

