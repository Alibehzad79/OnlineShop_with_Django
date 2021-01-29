# Generated by Django 3.1.5 on 2021-01-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0023_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default='100.000', max_length=500, null=True, verbose_name='قیمت'),
        ),
    ]
