# Generated by Django 4.0.7 on 2022-11-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_qna_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='qna_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
