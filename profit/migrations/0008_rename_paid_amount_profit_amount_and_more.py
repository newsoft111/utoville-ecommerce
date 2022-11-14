# Generated by Django 4.1.3 on 2022-11-14 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderitem_shipping_fee'),
        ('profit', '0007_alter_profit_payment_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profit',
            old_name='paid_amount',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='profit',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='profit',
            name='shipping_fee',
        ),
        migrations.AddField(
            model_name='profit',
            name='order_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.orderitem'),
            preserve_default=False,
        ),
    ]
