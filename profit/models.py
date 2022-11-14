from django.db import models
from datetime import date
from django.conf import settings
from datetime import datetime
from order.models import OrderItem
# Create your models here.


class ProfitDone(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	total_profit_amount=models.DecimalField(max_digits=14, decimal_places=2)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	total_payment_fee = models.DecimalField(max_digits=14, decimal_places=2)
	profit_done_amount=models.DecimalField(max_digits=14, decimal_places=2)
	total_shipping_fee = models.DecimalField(max_digits=14, decimal_places=2)

	class Meta:
		db_table = 'ecommerce_profit_done'


class ProfitManager(models.Manager):
	def get_queryset(self):
		return super(ProfitManager, self).get_queryset().filter(profit_done=None)

class Profit(models.Model):
	order_item = models.ForeignKey(
			OrderItem,
			on_delete=models.CASCADE,
	)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	charge_amount = models.DecimalField(max_digits=14, decimal_places=2)
	payment_fee = models.DecimalField(max_digits=14, decimal_places=2)
	profit_amount = models.DecimalField(max_digits=14, decimal_places=2)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	profit_done = models.ForeignKey(
			ProfitDone,
			on_delete=models.CASCADE,
			null=True
	)
	
	objects = ProfitManager()
	class Meta:
		db_table = 'ecommerce_profit'
	
