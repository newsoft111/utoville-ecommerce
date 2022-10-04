from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from datetime import datetime


def upload_to(instance, filename):
	nowDate = datetime.now().strftime("%Y/%m/%d")
	return '/'.join([str(instance.id), instance.folder , nowDate, filename])

class User(AbstractBaseUser, PermissionsMixin):
	id = models.AutoField(primary_key=True, db_column='mb_seq')
	username = models.CharField(max_length=200,unique=True, db_column='mb_id')
	password = models.CharField(max_length=200, db_column='mb_password')
	last_login = None
	is_superuser = None
	mbm_seq = models.PositiveIntegerField(null=True)
	ctl_seq1 = models.PositiveIntegerField(null=True)
	ctl_seq2 = models.PositiveIntegerField(null=True)
	ctl_seq3 = models.PositiveIntegerField(null=True)
	ctl_seq4 = models.PositiveIntegerField(null=True)
	mb_name = models.CharField(max_length=100)
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

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	objects = UserManager()

	class Meta:
		db_table = 'member_tb'

