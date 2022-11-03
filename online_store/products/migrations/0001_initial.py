# Generated by Django 4.1.1 on 2022-09-18 06:32

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=products.models.user_directory_path, verbose_name='photo')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'catalog',
                'verbose_name_plural': 'catalogs',
            },
        ),
        migrations.CreateModel(
            name='SubCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_catalogs', to='products.catalog', verbose_name='catalog')),
            ],
            options={
                'verbose_name': 'sub catalog',
                'verbose_name_plural': 'sub catalogs',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name product')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='price')),
                ('count', models.IntegerField(default=0, verbose_name='count product')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create data')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update data')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.catalog', verbose_name='catalog')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='PhotoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=products.models.photo_product_directory_path, verbose_name='photo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'photo product',
                'verbose_name_plural': 'photo products',
            },
        ),
    ]