from django.db import models
import uuid
from product.models import *
from account.models import UserShippingAddress

# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	pg_uid = models.CharField(max_length=255, null=True)
	ordered_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	shpping_address = models.ForeignKey(
			UserShippingAddress,
			on_delete=models.CASCADE,
			null=True
	)
	is_paid=models.BooleanField(default=False)
	paid_at = models.DateTimeField(null=True)

	class Meta:
		db_table = 'ecommerce_order'


class OrderItem(models.Model):
	order = models.ForeignKey(
			Order,
			on_delete=models.CASCADE
	)
	order_uid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=True)
	is_cancelled=models.BooleanField(default=False)
	cancelled_at = models.DateTimeField(null=True)
	is_refunded = models.BooleanField(default=False)
	refunded_at = models.DateTimeField(null=True)
	is_visited = models.BooleanField(default=False)
	visit_at = models.DateTimeField(null=True)
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
	

	class Meta:
		db_table = 'ecommerce_order_item'

	def sub_total_price(self):
		if self.variant is not None:
			return (self.product_price + self.variant_price) * self.ordered_quantity
		else:
			return self.product_price * self.ordered_quantity
