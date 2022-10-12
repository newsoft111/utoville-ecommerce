from django.db import models
from product.models import Product, ProductVariantValue
from datetime import datetime
from django.conf import settings

# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
				null=True, 
				blank=True
	)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

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
	active = models.BooleanField(default=True)

	class Meta:
		db_table = 'ecommerce_cart_item'

	def sub_total(self):
		return (self.product.price + self.variant_value.price) * self.quantity

	def __str__(self):
		return self.product

