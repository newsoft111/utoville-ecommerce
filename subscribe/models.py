from django.db import models
import uuid
from product.models import *
from account.models import UserShippingAddress

# Create your models here.
# class Subscribe(models.Model):
# 	user = models.ForeignKey(
# 			settings.AUTH_USER_MODEL,
# 			on_delete=models.CASCADE,
# 	)
# 	billing_key = models.CharField(max_length=255, null=True)
# 	subscribed_at = models.DateTimeField(auto_now_add=True, auto_now=False)

# 	class Meta:
# 		db_table = 'ecommerce_order'


# class SubscribeItem(models.Model):
# 	subscribe = models.ForeignKey(
# 			Subscribe,
# 			on_delete=models.CASCADE
# 	)
# 	is_unsubscribe = models.BooleanField(default=False)
# 	unsubscribed_at = models.DateTimeField(null=True)

# 	product = models.ForeignKey(
# 			Product,
# 			on_delete=models.CASCADE,
# 	)
# 	product_name = models.CharField(max_length=255)
# 	product_price = models.PositiveIntegerField()
# 	variant = models.CharField(max_length=255, null=True)
# 	variant_value = models.CharField(max_length=255, null=True)
# 	variant_price = models.PositiveIntegerField(null=True)
# 	ordered_quantity = models.PositiveIntegerField()
# 	shipped_quantity = models.PositiveIntegerField(default=0)
	

# 	class Meta:
# 		db_table = 'ecommerce_order_item'

# 	def sub_total_price(self):
# 		if self.variant is not None:
# 			return (self.product_price + self.variant_price) * self.ordered_quantity
# 		else:
# 			return self.product_price * self.ordered_quantity
