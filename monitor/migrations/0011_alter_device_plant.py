# Generated by Django 3.2 on 2021-04-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_alter_device_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='plant',
            field=models.ManyToManyField(blank=True, to='monitor.Plant'),
        ),
    ]
