from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import *
from django.core.paginator import Paginator
from datetime import datetime, timedelta, date
from django.views.generic import View
import json
from util.views import cache

# Create your views here.

@login_required(login_url="account:seller_login")
def seller_order_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}
	q = Q()
	q &= Q(product__user = request.user)
	q &= Q(order__payment__is_paid = True)
	order_item_list =  OrderItem.objects.filter(q).order_by( "-id")
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(order_item_list, 12)
	order_item_list = pagenator.get_page(page)

	return render(request, 'seller/order/order_list.html',{
		"seo":seo,
		'order_item_list': order_item_list
	})



@login_required(login_url="account:seller_login")
def seller_order_detail(request, order_item_id):
	seo = {
		'title': "상품주문정보 조회 - 유토빌",
	}
	q = Q()
	q &= Q(pk = order_item_id)

	order_item_obj =  get_object_or_404(OrderItem, q)

	return render(request, 'seller/order/order_detail.html',{
		"seo":seo,
		'order_item_obj': order_item_obj
	})


def seller_order_edit_status(request):
	jsonData = json.loads(request.body)
	event_type  = jsonData.get('event_type')
	order_item_id = jsonData.get('order_item_id')

	if event_type == '' or event_type is None:
		return JsonResponse({
			'result': '201',
			'result_text': '유형을 선택해주세요.'
		})

	order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)

	result = seller_update_status(query_set=order_item_objs, event_type=event_type)
	return JsonResponse(result)
	

def seller_update_status(query_set, event_type):
	if event_type == '배달완료':
		query_set.update(
			is_delivered = True, 
			delivered_at = datetime.now(),
			order_item_status = '배달완료'
		)
		return {
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		}

	elif event_type == '주문취소요청':
		query_set.update(
			is_refund_requested = True, 
			refund_requested_at = datetime.now(),
			order_item_status = '주문취소요청'
		)
		return {
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		}

	elif event_type == '주문접수':
		query_set.update(
			is_responded = True, 
			responded_at = datetime.now(),
			order_item_status = '주문접수'
		)

		return {
			'result': '200',
			'result_text': '접수가 완료되었습니다.'
		}


	else:
		return {
			'result': '201',
			'result_text': '알수 없는 오류입니다. 다시시도 해주세요.'
		}


class SellerOrderPreview(View):
	def get(self, request):
		self.end_date = datetime.now() + timedelta(1)

		q = Q()
		q &= Q(product__user=request.user)
		q &= Q(order__payment__is_paid = True)

		self.start_date = self.end_date - timedelta(days=7)
		q &= Q(order__payment__paid_at__range = [self.start_date, self.end_date])

		if request.GET.get('cache') == 'reload':
			order_items = OrderItem.objects.filter(q)
		else:
			order_items_cache = cache.get(f'{request.user}_order_items')
			if order_items_cache is not None:
				order_items = order_items_cache
			else:
				order_items = OrderItem.objects.filter(q)
		
		#월별
		if request.GET.get('standard') == 'Monthly':
			self.date_format = "%b"
			chart_data = self.monthly()
			#cache_data = cache.get(f'{request.user}_monthly')
			#if cache_data is not None:
			#	chart_data = cache_data
			#else:
			#	cache.put(f'{request.user}_monthly', chart_data)
		
		#일별
		else:
			self.date_format = "%a"
			chart_data = self.weekly()
			#cache_data = cache.get(f'{request.user}_weekly')
			#if cache_data is not None:
			#	chart_data = cache_data
			#else:
				
			#	cache.put(f'{request.user}_weekly', chart_data)


		total_price = 0
		for items in order_items:
			chart_data[items.order.payment.paid_at.strftime(self.date_format)] += 1
			total_price += items.sub_total_price()
			
		return JsonResponse({
			"chart_data": [{"x": key, "y": value} for key, value in chart_data.items()],
			'count': format(order_items.count(), ',')
		})

	def weekly(self):
		preview_data = {}
		def daterange(start_date, end_date):
			for n in range(int((end_date - start_date).days)):
				yield self.start_date + timedelta(n)

		for single_date in daterange(self.start_date, self.end_date):
			preview_data[single_date.strftime(self.date_format)] = 0
			
		return preview_data

	def monthly(self):
		preview_data = {}
		month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

		for month in month_list:
			preview_data[month] = 0

		return preview_data

