# Generated by Django 4.1.3 on 2022-11-11 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
