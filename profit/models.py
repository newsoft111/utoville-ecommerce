from django.db import models
from datetime import date
from django.conf import settings
from datetime import datetime
# Create your models here.


class Profit(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	amount = models.IntegerField()
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	payment_fee = models.DecimalField(max_digits = 2, decimal_places = 1, default=0.0)
	shipping_fee = models.PositiveIntegerField()
	profit_done = models.BooleanField(default=False)

	objects = models.Manager()
	
	class Meta:
		db_table = 'ecommerce_profit'


class ProfitDone(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	amount = models.IntegerField()
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	payment_fee = models.DecimalField(max_digits = 2, decimal_places = 1, default=0.0)
	shipping_fee = models.PositiveIntegerField()

	class Meta:
		db_table = 'ecommerce_profit_done'