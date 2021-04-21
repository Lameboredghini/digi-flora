# Generated by Django 3.2 on 2021-04-21 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0004_device_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='unique_id',
            field=models.SlugField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
