# Generated by Django 4.1.3 on 2022-11-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=14),
            preserve_default=False,
        ),
    ]