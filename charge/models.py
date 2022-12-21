from django.db import models
from django.conf import settings

# Create your models here.
class Payment(models.Model):
	txnid = models.CharField(max_length=255, null=True, unique=True)
	refno = models.CharField(max_length=255, null=True, unique=True)
	paid_at = models.DateTimeField(null=True)
	paid_amount = models.DecimalField(max_digits=14, decimal_places=2, null=True)
	referrer = models.CharField(max_length=200, default="homecare")
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)

	
	class Meta:
		db_table = 'charge_payment'


class Refund(models.Model):
	is_refunded = models.BooleanField(default=False)
	refunded_at = models.DateTimeField(null=True)

	
	class Meta:
		db_table = 'charge_refund'
