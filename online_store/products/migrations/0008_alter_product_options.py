# Generated by Django 4.1.1 on 2022-10-03 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_catalog_photo_photocatalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
