# Generated by Django 4.0.6 on 2022-10-05 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_option_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='option_json',
        ),
    ]