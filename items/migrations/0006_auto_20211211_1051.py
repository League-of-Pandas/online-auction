# Generated by Django 3.1.4 on 2021-12-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20211210_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=10000),
        ),
    ]
