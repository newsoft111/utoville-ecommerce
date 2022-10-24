# Generated by Django 4.0.7 on 2022-10-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_remove_productqna_status_productqna_deleted_at_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(related_name='order_orderitem_set', through='order.OrderItem', to='product.productvariantvalue'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='pg_uid',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variant_value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariantvalue'),
        ),
    ]
