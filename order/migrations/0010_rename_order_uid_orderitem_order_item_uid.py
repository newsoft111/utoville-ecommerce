# Generated by Django 4.1.3 on 2022-12-15 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0009_alter_order_payment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="order_uid",
            new_name="order_item_uid",
        ),
    ]
