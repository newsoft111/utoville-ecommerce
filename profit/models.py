from django.db import models
from datetime import date
from django.conf import settings
from datetime import datetime
from order.models import OrderItem
# Create your models here.



class Profit(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	total_charge_amount=models.DecimalField(max_digits=14, decimal_places=2, default=0)
	total_shipping_fee = models.DecimalField(max_digits=14, decimal_places=2, default=0)
	total_charge_fee = models.DecimalField(max_digits=14, decimal_places=2, default=0)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	is_done = models.BooleanField(default=False)
	memo = models.CharField(max_length=255, null=True)
	status = models.CharField(max_length=255, default='정산대기')
	total_profit_amount=models.DecimalField(max_digits=14, decimal_places=2, default=0)

	class Meta:
		db_table = 'ecommerce_profit'



class ProfitDetail(models.Model):
	order_item = models.ForeignKey(
			OrderItem,
			on_delete=models.CASCADE,
	)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	charge_amount = models.DecimalField(max_digits=14, decimal_places=2) #결제금액
	charge_fee = models.DecimalField(max_digits=14, decimal_places=2) #결제수수료
	shipping_fee = models.DecimalField(max_digits=14, decimal_places=2)
	profit_amount = models.DecimalField(max_digits=14, decimal_places=2) #정산금액
	profit = models.ForeignKey(
			Profit,
			on_delete=models.CASCADE,
	)
	
	class Meta:
		db_table = 'ecommerce_profit_detail'
	
