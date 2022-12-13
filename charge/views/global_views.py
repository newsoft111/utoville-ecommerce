from django.shortcuts import render
from ..models import *
from revenue.models import *
from order.models import *
from profit.models import Profit as ProfitModel
from django.http import JsonResponse


def call_back(request):
	#이거 그대로 쓰면 안되고 pg사 커스텀 데이터에 order_item_id 리스트 로 넘긴후 Revenue 에 넘겨줘야함
	order_item_id =  OrderItem.objects.filter(order=1)
	order_item_id_values = order_item_id.values_list('id', flat=True).order_by( "-id")
	
	Revenue(order_item_id_values, 'payment').new_data()
	Profit(order_item_id_values, 'payment').new_data()

	order_item_id = order_item_id.update(order_item_status='접수대기')

	return JsonResponse({
		'result': '200', 
		'result_text': '성공'
	})



class Profit:
	def __init__(self, order_item_id, event_type):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
		self.event_type = event_type

	def new_data(self):
		for order_item_obj in self.order_item_objs:
			charge_amount = order_item_obj.sub_total_price()
			payment_fee=0
			payment_fee = round(charge_amount*payment_fee, 2)

			profit_obj = ProfitModel.objects.create(
				order_item=order_item_obj,
				seller=order_item_obj.product.user,
				charge_amount=charge_amount if self.event_type=='payment' else -charge_amount,
				payment_fee=payment_fee,
				profit_amount=round(charge_amount-payment_fee, 2),
			)



class Revenue:
	def __init__(self, order_item_id, event_type):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
		self.event_type = event_type
	

	def new_data(self):
		self.admin_update()
		self.seller_update()

		
	def admin_update(self):
		revenue_admin_obj, created = RevenueAdmin.objects.get_or_create(date=date.today(), )
		for order_item_obj in self.order_item_objs:
			if self.event_type == 'payment':
				revenue_admin_obj.payment_amount += order_item_obj.sub_total_price()
				revenue_admin_obj.order_count += 1

			elif self.event_type == 'refund':
				revenue_admin_obj.refund_amount += order_item_obj.sub_total_price()
				revenue_admin_obj.order_count -= 1

			else:
				print('오류')
		revenue_admin_obj.save()

	def seller_update(self):
		revenue_admin_obj, created = RevenueSeller.objects.get_or_create(date=date.today(), seller=self.order_item_objs[0].product.user)

		for order_item_obj in self.order_item_objs:
			if self.event_type == 'payment':
				revenue_admin_obj.payment_amount += order_item_obj.sub_total_price()
				revenue_admin_obj.order_count += order_item_obj.ordered_quantity

			elif self.event_type == 'refund':
				revenue_admin_obj.refund_amount += self.amount
				
			else:
				print('오류')
			revenue_admin_obj.save()