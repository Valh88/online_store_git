# Generated by Django 4.1.1 on 2022-10-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_delivery_alter_order_type_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.BooleanField(verbose_name='type delivery'),
        ),
    ]
