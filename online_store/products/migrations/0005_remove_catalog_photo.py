# Generated by Django 4.1.1 on 2022-09-30 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_catalog_select_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='photo',
        ),
    ]
