from django.db import models

class HouseCheckItem(models.Model):
	item = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_house_check_item'