from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.validators import MinValueValidator


		
class UserManager(BaseUserManager):
	def create_user(self,mb_id,password,**other_fields):
		if not mb_id:
				raise ValueError(_('Please provide an mb_id address'))
		mb_id=self.normalize_mb_id(mb_id)
		user=self.model(mb_id=mb_id,**other_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,mb_id,password,**other_fields):
		other_fields.setdefault('is_staff',True)
		other_fields.setdefault('is_superuser',True)
		other_fields.setdefault('is_active',True)
		if other_fields.get('is_staff') is not True:
						raise ValueError(_('Please assign is_staff=True for superuser'))
		if other_fields.get('is_superuser') is not True:
						raise ValueError(_('Please assign is_superuser=True for superuser'))
		return self.create_user(mb_id,password,**other_fields)

	


def upload_to(instance, filename):
	nowDate = datetime.now().strftime("%Y/%m/%d")
	return '/'.join([str(instance.id), instance.folder , nowDate, filename])

class User(AbstractBaseUser,PermissionsMixin):
	password = None
	last_login = None
	is_superuser = None
	mb_seq = models.AutoField(primary_key=True)
	mbm_seq = models.PositiveIntegerField(null=True)
	ctl_seq1 = models.PositiveIntegerField(null=True)
	ctl_seq2 = models.PositiveIntegerField(null=True)
	ctl_seq3 = models.PositiveIntegerField(null=True)
	ctl_seq4 = models.PositiveIntegerField(null=True)
	mb_id = models.CharField(max_length=200,unique=True)
	mb_name = models.CharField(max_length=100)
	mb_password = models.CharField(max_length=200)
	mb_type = models.CharField(max_length=1)
	mb_status = models.CharField(max_length=1)
	mb_profile = models.ImageField(upload_to=upload_to, default="avater.jpg")
	mb_profile_org = models.CharField(max_length=300)
	mb_email = models.CharField(max_length=200)
	mb_phone = models.CharField(max_length=100)
	mb_active = models.CharField(max_length=1)
	mb_position_seq = models.PositiveIntegerField(null=True)
	mb_position = models.CharField(max_length=200)
	mb_fcm = models.CharField(max_length=200)
	mb_del_date = models.DateTimeField(null=True)
	mb_regdate = models.DateTimeField(default=datetime.now)

	objects=UserManager()

	USERNAME_FIELD='mb_id'
	REQUIRED_FIELDS=[]

	def __str__(self):
		return self.mb_id

	class Meta:
		managed = True
		db_table = 'member_tb'

