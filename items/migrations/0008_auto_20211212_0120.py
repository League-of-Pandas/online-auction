# Generated by Django 3.1.4 on 2021-12-12 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20211211_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Vehicles', 'Vehicles'), ('Coins & Bullion', 'Coins & Bullion'), ('Art', 'Art'), ('Furniture', 'Furniture'), ('Electronics', 'Electronics'), ('Jewelry', 'Jewelry')], default='Vehicles', max_length=100),
        ),
    ]