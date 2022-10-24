from django.db import models
from product.models import *
from account.models import UserShippingAddress

# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	pg_uid = models.CharField(max_length=255, blank=True)
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
	order_item = models.ManyToManyField(
				Product,
				related_name="order_orderitem_set",
				through='OrderItem'
	)

	class Meta:
		db_table = 'ecommerce_order'


class OrderItem(models.Model):
	order = models.ForeignKey(
			Order,
			on_delete=models.CASCADE
	)
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE,
	)
	product_name = models.CharField(max_length=255)
	product_price = models.PositiveIntegerField()
	variant = models.CharField(max_length=255, null=True)
	variant_value = models.CharField(max_length=255, null=True)
	variant_price = models.PositiveIntegerField(null=True)
	quantity = models.PositiveIntegerField()
	

	class Meta:
		db_table = 'ecommerce_order_item'
