from django.shortcuts import render
from .models import *
from order.models import *
from datetime import date

class Revenue:
	def __init__(self, order_item_id, amount, event_type):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
		self.amount = amount
		print(type(self.amount))
		self.event_type = event_type

		self.admin_update()
		self.seller_update()
	
	def admin_update(self):
		revenue_admin_obj, created = RevenueAdmin.objects.get_or_create(date=date.today())
		if self.event_type == 'payment':
			revenue_admin_obj.payment_amount += self.amount
			revenue_admin_obj.order_count += self.order_item_objs.count()

		elif self.event_type == 'refund':
			revenue_admin_obj.refund_amount += self.amount

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