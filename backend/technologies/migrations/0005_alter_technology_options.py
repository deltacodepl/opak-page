# Generated by Django 3.2.19 on 2023-07-04 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0004_alter_technology_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['id'], 'verbose_name': 'Technology', 'verbose_name_plural': 'Technologies'},
        ),
    ]
