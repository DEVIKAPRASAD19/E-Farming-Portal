# Generated by Django 5.0 on 2024-09-26 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0016_registeruser_created_at_registeruser_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.registeruser'),
        ),
    ]
