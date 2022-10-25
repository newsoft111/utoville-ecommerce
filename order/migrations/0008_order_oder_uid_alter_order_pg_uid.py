# Generated by Django 4.0.7 on 2022-10-25 02:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_orderitem_variant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='oder_uid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pg_uid',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
