from django.db import models
from product.models import Product, ProductVariantValue
from datetime import datetime
from django.conf import settings

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

	def delete(self):
		self.is_deleted = True
		self.deleted_at = datetime.now()
		self.save()

