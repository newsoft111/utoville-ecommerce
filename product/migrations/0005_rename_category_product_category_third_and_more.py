# Generated by Django 4.0.6 on 2022-10-07 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0004_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_third',
        ),
        migrations.AddField(
            model_name='product',
            name='category_first',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.categoryfirst'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category_second',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.categorysecond'),
            preserve_default=False,
        ),
    ]