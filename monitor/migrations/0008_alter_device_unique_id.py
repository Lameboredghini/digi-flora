# Generated by Django 3.2 on 2021-04-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20210422_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='unique_id',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
