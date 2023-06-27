from django.db import models
import uuid
from product.models import *
from account.models import UserShippingAddress


class SubscribeBillingKey(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	billing_key = models.CharField(max_length=255, null=True)

	class Meta:
		db_table = 'ecommerce_subcribe_billing_key'


class SubscribeItem(models.Model):
	billing_key = models.ForeignKey(
			SubscribeBillingKey,
			on_delete=models.CASCADE
	)
	is_subscribe = models.BooleanField(default=False)
	subscribed_at = models.DateTimeField()

	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE,
	)
	product_name = models.CharField(max_length=255)
	product_price = models.PositiveIntegerField()
	variant = models.CharField(max_length=255, null=True)
	variant_value = models.CharField(max_length=255, null=True)
	variant_price = models.PositiveIntegerField(null=True)
	ordered_quantity = models.PositiveIntegerField()
	shipped_quantity = models.PositiveIntegerField(default=0)
	

	class Meta:
		db_table = 'ecommerce_subcribe_item'

	def sub_total_price(self):
		if self.variant is not None:
			return (self.product_price + self.variant_price) * self.ordered_quantity
		else:
			return self.product_price * self.ordered_quantity
