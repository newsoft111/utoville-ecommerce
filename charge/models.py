from django.db import models
from django.conf import settings

# Create your models here.
class Payment(models.Model):
	payment_uid = models.CharField(max_length=255, null=True, unique=True)
	is_paid=models.BooleanField(default=False)
	paid_at = models.DateTimeField(null=True)
	paid_amount = models.DecimalField(max_digits=14, decimal_places=2)

	
	class Meta:
		db_table = 'ecommerce_payment'


class Refund(models.Model):
	is_refunded = models.BooleanField(default=False)
	refunded_at = models.DateTimeField(null=True)

	
	class Meta:
		db_table = 'ecommerce_refund'
