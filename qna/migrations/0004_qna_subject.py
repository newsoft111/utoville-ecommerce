# Generated by Django 4.0.7 on 2022-11-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]