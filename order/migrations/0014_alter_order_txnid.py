# Generated by Django 4.1.3 on 2022-12-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0013_alter_order_txnid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="txnid",
            field=models.CharField(
                default=15353269567119233517, max_length=255, verbose_name="주문번호"
            ),
        ),
    ]
