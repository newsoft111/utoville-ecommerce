# Generated by Django 4.1.3 on 2022-11-14 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0010_rename_profit_done_amount_profitdone_sum_profit_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profitdone',
            old_name='sum_profit_amount',
            new_name='profit_done_amount',
        ),
    ]
