from django.db import models
from django.conf import settings

# Create your models here.
class Payment(models.Model):
	pg_uid = models.CharField(max_length=255, null=True, unique=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	is_paid=models.BooleanField(default=False)
	paid_at = models.DateTimeField(null=True)
	used_point = models.PositiveIntegerField(default=0)

	class Meta:
		db_table = 'ecommerce_payment'