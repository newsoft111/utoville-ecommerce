# Generated by Django 4.1.3 on 2022-11-11 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('payment_fee', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=14)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ecommerce_profit_done',
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('payment_fee', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=14)),
                ('is_done', models.BooleanField(default=False)),
                ('profit_done', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profit.profitdone')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ecommerce_profit',
            },
        ),
    ]
