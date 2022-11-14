from django.db import models
from datetime import date
from django.conf import settings
from datetime import datetime
# Create your models here.


class ProfitDone(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	paid_amount = models.DecimalField(max_digits=14, decimal_places=2)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	payment_fee = models.DecimalField(max_digits = 2, decimal_places = 1, default=0.0)
	shipping_fee = models.DecimalField(max_digits=14, decimal_places=2)

	class Meta:
		db_table = 'ecommerce_profit_done'


class ProfitManager(models.Manager):
	def get_queryset(self):
		return super(ProfitManager, self).get_queryset().filter(is_done=False)

class Profit(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	paid_amount = models.DecimalField(max_digits=14, decimal_places=2)
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	payment_fee = models.DecimalField(max_digits = 2, decimal_places = 1, default=0.0)
	shipping_fee = models.DecimalField(max_digits=14, decimal_places=2)
	is_done = models.BooleanField(default=False)
	profit_done = models.ForeignKey(
			ProfitDone,
			on_delete=models.CASCADE,
			null=True
	)
	
	objects = ProfitManager()
	class Meta:
		db_table = 'ecommerce_profit'
	
	def get_profit_amount(self):
		return round((self.paid_amount*(1-self.payment_fee)), 2)
