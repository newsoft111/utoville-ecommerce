# Generated by Django 4.0.7 on 2022-10-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_productqna_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productqna',
            name='status',
        ),
        migrations.AddField(
            model_name='productqna',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='productqna',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]