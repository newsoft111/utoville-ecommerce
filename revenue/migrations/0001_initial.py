# Generated by Django 4.1.3 on 2022-11-09 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RevenueAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('payment_amount', models.PositiveIntegerField(default=0)),
                ('refunt_amount', models.PositiveIntegerField(default=0)),
                ('order_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RevenueSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('payment_amount', models.PositiveIntegerField(default=0)),
                ('refunt_amount', models.PositiveIntegerField(default=0)),
                ('order_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
