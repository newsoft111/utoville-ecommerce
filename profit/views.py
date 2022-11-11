from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Profit as ProfitModel
from django.core.paginator import Paginator
from django.http import JsonResponse
from order.models import *
import json, re

class Profit:
	def __init__(self, order_item_id):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)

	def new_data(self):
		for order_item_obj in self.order_item_objs:
			profit_obj = ProfitModel.objects.create(
				seller=order_item_obj.product.user,
				paid_amount=order_item_obj.sub_total_price(),
				shipping_fee=0,
				payment_fee=0
			)