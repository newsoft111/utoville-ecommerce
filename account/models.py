from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.validators import MinValueValidator


		
class UserManager(BaseUserManager):
	def create_user(self,email,password,**other_fields):
		if not email:
				raise ValueError(_('Please provide an email address'))
		email=self.normalize_email(email)
		user=self.model(email=email,**other_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,email,password,**other_fields):
		other_fields.setdefault('is_staff',True)
		other_fields.setdefault('is_superuser',True)
		other_fields.setdefault('is_active',True)
		if other_fields.get('is_staff') is not True:
						raise ValueError(_('Please assign is_staff=True for superuser'))
		if other_fields.get('is_superuser') is not True:
						raise ValueError(_('Please assign is_superuser=True for superuser'))
		return self.create_user(email,password,**other_fields)

def upload_to(instance, filename):
	nowDate = datetime.now().strftime("%Y/%m/%d")
	return '/'.join([str(instance.id), instance.folder , nowDate, filename])

class User(AbstractBaseUser,PermissionsMixin):
	email=models.EmailField(unique=True)
	username= None
	first_name = None
	last_name = None
	point = models.PositiveIntegerField(default=0)
	nickname = models.CharField(u'닉네임', max_length=10, blank=False, unique=True, default='')
	full_name = models.CharField(u'이름', max_length=10, blank=True)
	phone_number = models.CharField(max_length=255,blank=True)
	birth_year = models.IntegerField(null=True)
	is_staff=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	is_verify=models.BooleanField(default=False)
	joined_at = models.DateTimeField(default=datetime.now)
	folder = 'avater'
	avater = models.ImageField(upload_to=upload_to, default="avater.jpg")

	objects=UserManager()

	USERNAME_FIELD='email'
	REQUIRED_FIELDS=[]

	def __str__(self):
			return self.email
