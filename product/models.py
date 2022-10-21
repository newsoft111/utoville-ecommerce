from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import datetime
from category.models import *
from decimal import Decimal



class ModelDeleteManager(models.Manager):
	def get_queryset(self):
		return super(ModelDeleteManager, self).get_queryset().filter(is_deleted=False)


def upload_to(instance, filename):
	nowDate = datetime.now().strftime("%Y/%m/%d")
	return '/'.join([instance.folder, str(instance.product.id), nowDate, filename])


class Product(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
	)
	category_first = models.ForeignKey(
				CategoryFirst,
				on_delete=models.CASCADE,
	)
	category_second = models.ForeignKey(
				CategorySecond,
				on_delete=models.CASCADE,
	)
	category_third = models.ForeignKey(
				CategoryThird,
				on_delete=models.CASCADE,
	)
	name = models.CharField(max_length=255)
	content = models.TextField()
	price = models.PositiveIntegerField(default=0)
	discount = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True)
	rating = models.DecimalField(max_digits = 2, decimal_places = 1, default=0.0)
	rating_count = models.PositiveIntegerField(default=0)
	review = models.ManyToManyField(
				settings.AUTH_USER_MODEL,
				related_name="my_review",
				blank=True,
				through='ProductReview'
	)


	objects = ModelDeleteManager()

	class Meta:
		db_table = 'ecommerce_product'


class ProductArea(models.Model):
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	area = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_product_area'

	def __str__(self) :
		return self.area


class ProductVariant(models.Model):
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	variant = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_product_variant'

	def __str__(self) :
		return self.variant


class ProductVariantValue(models.Model):
	variant = models.ForeignKey(
			ProductVariant,
			on_delete=models.CASCADE
	)
	value = models.CharField(max_length=255)
	price = models.IntegerField(default=0)

	class Meta:
		db_table = 'ecommerce_product_variant_value'



class ProductImage(models.Model):
	image = models.FileField(upload_to=upload_to)
	folder = 'ecommerce/product'
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	
	class Meta:
		db_table = 'ecommerce_product_image'



class ProductThumbnail(models.Model):
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)

	folder = 'ecommerce/product'
	thumbnail = ProcessedImageField(
				upload_to=upload_to,
				processors=[ResizeToFill(800, 800)],
	)

	class Meta:
		db_table = 'ecommerce_product_thumbnail'


class ProductReview(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
	)
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	review = models.TextField()
	rating = models.PositiveIntegerField()
	created_at = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = 'ecommerce_product_review'

	def save(self, *args, **kwargs):
		try:
			self.product.rating = ((Decimal(self.product.rating) * self.product.rating_count) + Decimal(self.rating)) / (self.product.rating_count+1)
			self.product.rating_count += 1
			self.product.save()
		except:
			pass

		super().save(*args, **kwargs)


class ProductQnA(models.Model):
	product = models.ForeignKey(
			Product,
			on_delete=models.CASCADE
	)
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
	)
	question = models.TextField()
	answer = models.TextField()
	questioned_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	answered_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True)

	objects = ModelDeleteManager()

	class Meta:
		db_table = 'ecommerce_product_qna'