# Generated by Django 3.2.19 on 2023-07-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0003_auto_20230703_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['-id'], 'verbose_name': 'Technology', 'verbose_name_plural': 'Technologies'},
        ),
    ]
