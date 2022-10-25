# Generated by Django 4.0.7 on 2022-10-25 02:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rename_oder_uid_order_order_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cancelled_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_cancelled',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_refunded',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_uid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refunded_at',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cancelled_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_refunded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_uid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='refunded_at',
            field=models.DateTimeField(null=True),
        ),
    ]
