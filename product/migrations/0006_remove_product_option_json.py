# Generated by Django 4.0.6 on 2022-10-05 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_img_productimage_image_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='option_json',
        ),
    ]