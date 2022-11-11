from django.db import models
from product.models import Product, ProductVariantValue
from datetime import datetime
from django.conf import settings
from decimal import Decimal

class ModelDeleteManager(models.Manager):
	def get_queryset(self):
		return super(ModelDeleteManager, self).get_queryset().filter(is_deleted=False)


class Cart(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
				null=True, 
				blank=True
	)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		db_table = 'ecommerce_cart'



class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
	quantity = models.PositiveIntegerField()
	variant_value = models.ForeignKey(
		ProductVariantValue, 
		on_delete=models.CASCADE,
		null=True, 
		blank=True
	)
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True)

	objects = ModelDeleteManager()

	class Meta:
		db_table = 'ecommerce_cart_item'

	def __str__(self):
		return self.product

	
	def sub_price(self):
		if self.variant_value is not None:
			return self.product.price + self.variant_value.price
		else:
			return self.product.price

	def sub_total_price(self):
		if self.variant_value is not None:
			print((self.product.price + self.variant_value.price))
			return Decimal(self.product.price + self.variant_value.price) * Decimal(self.quantity)
		else:
			return Decimal(self.product.price) * Decimal(self.quantity)