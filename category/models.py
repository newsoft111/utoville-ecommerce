from django.db import models
# Create your models here.

class CategoryFirst(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_first'



class CategorySecond(models.Model):
	parent = models.ForeignKey(
			CategoryFirst,
			on_delete=models.CASCADE
	)
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_second'



class CategoryThird(models.Model):
	parent = models.ForeignKey(
			CategorySecond,
			on_delete=models.CASCADE
	)
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_third'