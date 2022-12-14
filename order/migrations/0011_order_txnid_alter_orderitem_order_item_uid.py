# Generated by Django 4.1.3 on 2022-12-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0010_rename_order_uid_orderitem_order_item_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="txnid",
            field=models.CharField(
                default=17031155891999609325, max_length=255, verbose_name="주문번호"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order_item_uid",
            field=models.CharField(max_length=255, null=True, verbose_name="상품주문번호"),
        ),
    ]
