# Generated by Django 3.0.2 on 2020-04-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20200401_1301'),
        ('users', '0009_auto_20200405_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='shopping.Product'),
        ),
    ]
