from django.db import models
from datetime import date
from django.conf import settings
# Create your models here.
class RevenueAdmin(models.Model):
	date = models.DateField()
	payment_amount = models.PositiveIntegerField(default=0)
	refunt_amount = models.PositiveIntegerField(default=0)
	order_count = models.PositiveIntegerField(default=0)

	class Meta:
		db_table = 'ecommerce_revenue_admin'


class RevenueSeller(models.Model):
	seller = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	date = models.DateField()
	payment_amount = models.PositiveIntegerField(default=0)
	refunt_amount = models.PositiveIntegerField(default=0)
	order_count = models.PositiveIntegerField(default=0)

	class Meta:
		db_table = 'ecommerce_revenue_seller'