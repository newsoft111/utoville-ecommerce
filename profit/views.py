from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from order.models import *
import json, re

class Profit:
	def __init__(self, order_item_id):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
	
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