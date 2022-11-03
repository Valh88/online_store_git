# Generated by Django 4.1.1 on 2022-09-18 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=users.models.user_directory_path, verbose_name='avatar')),
                ('phone', models.CharField(max_length=12, verbose_name='phone')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='balance')),
                ('username', models.CharField(max_length=10, verbose_name='username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile user',
                'verbose_name_plural': 'profiles users',
            },
        ),
    ]