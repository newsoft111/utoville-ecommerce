from django.db import models
from django.conf import settings

# Create your models here.
class QnA(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
	)
	question = models.TextField()
	answer = models.TextField()
	questioned_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	answered_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		db_table = 'ecommerce_qna'