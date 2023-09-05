from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q, Sum, Avg
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json, re
import urllib

User = get_user_model()

class ProfitManage:
	def __init__(self, order_item_id, event_type):
		self.order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
		self.event_type = event_type

	def new_data(self):
		for order_item_obj in self.order_item_objs:
			charge_amount = order_item_obj.sub_total_price()
			charge_fee=0
			shipping_fee=0
			profit_amount=round(charge_amount-charge_fee-shipping_fee, 2)


			profit_obj, created = Profit.objects.get_or_create(seller=order_item_obj.product.user, is_done=False)

			profit_detail_obj = ProfitDetail.objects.create(
				order_item=order_item_obj,
				charge_amount=charge_amount if self.event_type=='payment' else -charge_amount,
				charge_fee=charge_fee,
				shipping_fee=shipping_fee,
				profit=profit_obj,
				profit_amount=profit_amount
			)


			profit_obj.total_paid_amount += charge_amount if self.event_type=='payment' else -charge_amount
			profit_obj.total_shipping_fee += shipping_fee
			profit_obj.total_payment_fee += charge_fee
			profit_obj.total_profit_amount += profit_amount
			profit_obj.save()



