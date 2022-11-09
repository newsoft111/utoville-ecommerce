# Generated by Django 4.1.3 on 2022-11-09 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revenue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenueseller',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revenueadmin',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='revenueseller',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='revenueadmin',
            table='ecommerce_revenue_admin',
        ),
        migrations.AlterModelTable(
            name='revenueseller',
            table='ecommerce_revenue_seller',
        ),
    ]
