from django.shortcuts import render
from ..models import *
from order.models import OrderItem
from django.http import JsonResponse
from revenue.views import RevenueManage
from profit.views import ProfitManage


def call_back(request):
	#이거 그대로 쓰면 안되고 pg사 커스텀 데이터에 order_item_id 리스트 로 넘긴후 Revenue 에 넘겨줘야함
	order_item_id =  OrderItem.objects.filter(order=1)
	order_item_id_values = order_item_id.values_list('id', flat=True).order_by( "-id")
	
	RevenueManage(order_item_id_values, 'payment').new_data()
	ProfitManage(order_item_id_values, 'payment').new_data()

	order_item_id = order_item_id.update(order_item_status='접수대기')

	return JsonResponse({
		'result': '200', 
		'result_text': '성공'
	})

