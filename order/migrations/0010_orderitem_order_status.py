# Generated by Django 4.0.7 on 2022-11-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rename_visited_at_orderitem_delivered_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
