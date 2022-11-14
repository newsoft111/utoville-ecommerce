from django.db import models
from django.conf import settings

# Create your models here.
class QnA(models.Model):
	user = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE,
	)
	qna_type = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	question = models.TextField()
	answer = models.TextField()
	questioned_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	answered_at = models.DateTimeField(null=True)

	class Meta:
		db_table = 'ecommerce_qna'