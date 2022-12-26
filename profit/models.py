from django.db import models
from datetime import date
from django.conf import settings
from datetime import datetime
from order.models import OrderItem
# Create your models here.



class Profit(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	total_charge_amount=models.DecimalField(max_digits=14, decimal_places=2)
	total_shipping_fee = models.DecimalField(max_digits=14, decimal_places=2)
	total_charge_fee = models.DecimalField(max_digits=14, decimal_places=2)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	is_done = models.BooleanField(default=False)
	memo = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	total_profit_amount=models.DecimalField(max_digits=14, decimal_places=2)

	class Meta:
		db_table = 'ecommerce_profit'


class ProfitManager(models.Manager):
	def get_queryset(self):
		return super(ProfitManager, self).get_queryset().filter(profit_done=None)

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
	
	objects = ProfitManager()
	class Meta:
		db_table = 'ecommerce_profit_detail'
	
