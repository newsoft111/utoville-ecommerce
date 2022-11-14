from django.db import models
import calendar
import time
from product.models import *
from account.models import UserShippingAddress
from charge.models import *
from decimal import Decimal

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
	total_price = models.DecimalField(max_digits=14, decimal_places=2)
	used_point = models.DecimalField(max_digits=14, decimal_places=2)

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
	is_responded = models.BooleanField(default=False, verbose_name="셀러가 주문에 응답했는지")
	responded_at = models.DateTimeField(null=True)
	is_refund_requested = models.BooleanField(default=False, verbose_name="셀러에게 환불요청 했는지")
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
	order_item_status = models.CharField(max_length=255)
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=14, decimal_places=2)
	variant = models.CharField(max_length=255, null=True)
	variant_value = models.CharField(max_length=255, null=True)
	variant_price = models.DecimalField(max_digits=14, decimal_places=2, null=True)
	ordered_quantity = models.PositiveIntegerField()
	shipped_quantity = models.PositiveIntegerField(default=0)
	is_subscribe = models.BooleanField(default=False)
	schedule_date= models.DateTimeField()
	shipping_fee = models.DecimalField(max_digits=14, decimal_places=2, default=0.0)

	class Meta:
		db_table = 'ecommerce_order_item'

	def sub_price(self):
		if self.variant is not None:
			return self.product_price + self.variant_price
		else:
			return self.product_price

	def sub_total_price(self):
		if self.variant is not None:
			print((self.product_price + self.variant_price))
			return Decimal(self.product_price + self.variant_price) * Decimal(self.ordered_quantity)
		else:
			return Decimal(self.product_price) * Decimal(self.ordered_quantity)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		order_uid = str(calendar.timegm(time.gmtime()))+str(self.pk)
		OrderItem.objects.filter(id=self.pk).update(order_uid=order_uid)
	