# Generated by Django 3.2.19 on 2023-07-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0002_auto_20230702_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='cols',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='rows',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
