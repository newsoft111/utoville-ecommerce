from django.db import models
from product.models import *
from account.models import UserShippingAddress

# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	pg_uid = models.CharField(max_length=255)
	ordered_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	shpping_address = models.ForeignKey(
			UserShippingAddress,
			on_delete=models.CASCADE,
			null=True
	)
	is_paid=models.BooleanField(default=False)
	paid_at = models.DateTimeField(null=True)
	is_cancelled=models.BooleanField(default=False)
	cancelled_at = models.DateTimeField(null=True)
	is_refunded=models.BooleanField(default=False)
	refunded_at = models.DateTimeField(null=True)
	item = models.ManyToManyField(
				ProductVariantValue,
				related_name="my_item",
				through='OrderItem'
	)

	class Meta:
		db_table = 'ecommerce_order'


class OrderItem(models.Model):
	order = models.ForeignKey(
			Order,
			on_delete=models.CASCADE
	)
	variant_value = models.ForeignKey(
			ProductVariantValue,
			on_delete=models.CASCADE
	)
	quantity = models.PositiveIntegerField()
	total_price = models.PositiveIntegerField()

	class Meta:
		db_table = 'ecommerce_order_item'
