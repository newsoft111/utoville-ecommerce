from django.db import models
from product.models import *

# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
	)
	pg_uid = models.CharField(max_length=255)
	ordered_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	shpping_address = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	status = models.CharField(max_length=255)
	item = models.ManyToManyField(
				ProductVariantValue,
				related_name="my_item",
				through='ProductArea'
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
