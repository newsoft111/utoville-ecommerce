from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse

class ModelDeleteManager(models.Manager):
	def get_queryset(self):
		return super(ModelDeleteManager, self).get_queryset().filter(is_deleted=False)

class Product(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
	)
	name = models.CharField(max_length=255)
	price = models.PositiveIntegerField(default=0)
	discount = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(default=datetime.now)
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True)
	objects = ModelDeleteManager()


	class Meta:
		managed = True
		db_table = 'ecommerce_product'
