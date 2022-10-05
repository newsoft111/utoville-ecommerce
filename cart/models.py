from django.db import models
from product.models import Product
from datetime import datetime

# Create your models here.

class Cart(models.Model):
	cart_id = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = 'ecommerce_cart'

	def __str__(self):
		return self.cart_id


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	active = models.BooleanField(default=True)

	class Meta:
		db_table = 'ecommerce_cart_item'

	def sub_total(self):
		return self.product.price * self.quantity

	def __str__(self):
		return self.product