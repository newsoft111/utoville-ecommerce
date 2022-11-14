from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Profit as ProfitModel
from django.core.paginator import Paginator
from django.http import JsonResponse
from order.models import *
import json, re

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