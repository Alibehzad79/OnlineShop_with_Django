# Generated by Django 3.1.5 on 2021-01-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0004_product_new_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_type',
            field=models.CharField(choices=[('جدید', 'جدید'), (' ', ' ')], default='null', max_length=200),
        ),
    ]
