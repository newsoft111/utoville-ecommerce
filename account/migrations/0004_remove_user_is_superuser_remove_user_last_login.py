# Generated by Django 4.0.6 on 2022-10-04 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
