# Generated by Django 4.1.3 on 2022-11-14 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profit',
            old_name='is_done',
            new_name='is_odone',
        ),
    ]
