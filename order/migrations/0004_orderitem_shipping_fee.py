# Generated by Django 4.1.3 on 2022-11-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14),
        ),
    ]
