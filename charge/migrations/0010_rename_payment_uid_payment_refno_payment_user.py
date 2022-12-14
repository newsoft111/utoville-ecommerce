# Generated by Django 4.1.3 on 2022-12-21 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("charge", "0009_alter_payment_referrer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="payment_uid",
            new_name="refno",
        ),
        migrations.AddField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
