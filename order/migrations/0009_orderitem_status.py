# Generated by Django 4.1.3 on 2022-11-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_orderitem_accepted_at_orderitem_is_accepted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(default='결제대기', max_length=255),
        ),
    ]
