# Generated by Django 4.1.3 on 2023-07-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoryfirst",
            name="is_display",
            field=models.BooleanField(default=False),
        ),
    ]
