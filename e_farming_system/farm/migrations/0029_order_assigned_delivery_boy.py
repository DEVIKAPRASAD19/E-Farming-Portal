# Generated by Django 5.0 on 2025-01-22 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0028_deliveryboydetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assigned_delivery_boy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_orders', to='farm.deliveryboydetail'),
        ),
    ]
