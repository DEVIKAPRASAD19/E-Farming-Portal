# Generated by Django 5.0 on 2024-10-17 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0014_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.crop')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.order')),
            ],
        ),
    ]
