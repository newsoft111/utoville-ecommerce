from django.db import models
import calendar
import time
from product.models import *
from account.models import UserShippingAddress
from charge.models import *


# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	ordered_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	shpping_address = models.ForeignKey(
			UserShippingAddress,
			on_delete=models.CASCADE,
			null=True
	)
	payment = models.ForeignKey(
		Payment,
		on_delete=models.CASCADE,
	)
	total_price = models.PositiveIntegerField(default=0)
	used_point = models.PositiveIntegerField(default=0)

	class Meta:
		db_table = 'ecommerce_order'


class OrderItem(models.Model):
	order = models.ForeignKey(
			Order,
			on_delete=models.CASCADE
	)
	order_uid = models.CharField(
		max_length=255,
		null=True
	)
	is_accepted = models.BooleanField(default=False)
	accepted_at = models.DateTimeField(null=True)
	is_refund_requested = models.BooleanField(default=False)
	refund_requested_at = models.DateTimeField(null=True)
	refund = models.ForeignKey(
		Refund,
		on_delete=models.CASCADE,
		null=True
	)
	is_delivered = models.BooleanField(default=False)
	delivered_at = models.DateTimeField(null=True)
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
	is_subscribe = models.BooleanField(default=False)
	schedule_date= models.DateTimeField()
	order_status = models.CharField(max_length=255)
	

	class Meta:
		db_table = 'ecommerce_order_item'

	def sub_price(self):
		if self.variant is not None:
			return self.product_price + self.variant_price
		else:
			return self.product_price

	def sub_total_price(self):
		if self.variant is not None:
			return (int(self.product_price) + int(self.variant_price)) * int(self.ordered_quantity)
		else:
			return int(self.product_price) * int(self.ordered_quantity)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		order_uid = str(calendar.timegm(time.gmtime()))+str(self.pk)
		OrderItem.objects.filter(id=self.pk).update(order_uid=order_uid)