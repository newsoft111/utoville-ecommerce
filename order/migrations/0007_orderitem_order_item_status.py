# Generated by Django 4.1.3 on 2022-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_accepted_at_orderitem_responded_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_item_status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
