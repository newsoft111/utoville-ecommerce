from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *
from django.db.models import Q, Sum
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from order.models import OrderItem

class RevenueManage:
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