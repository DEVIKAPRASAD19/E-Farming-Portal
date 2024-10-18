# Generated by Django 5.0 on 2024-10-17 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('place', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=6)),
                ('delivery_address', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('cod', 'Cash on Delivery'), ('online', 'Online Payment')], max_length=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(to='farm.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.registeruser')),
            ],
        ),
    ]
