# Generated by Django 3.2.19 on 2023-07-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='icon',
        ),
        migrations.AddField(
            model_name='technology',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
