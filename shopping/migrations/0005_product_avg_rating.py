# Generated by Django 3.0.2 on 2020-04-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_rating',
            field=models.FloatField(null=True),
        ),
    ]