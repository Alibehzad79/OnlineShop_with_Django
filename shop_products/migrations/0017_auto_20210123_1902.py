# Generated by Django 3.1.5 on 2021-01-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0016_product_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='new_type',
            field=models.CharField(choices=[('yes', 'بله'), ('no', 'خیر')], default='no', max_length=200, verbose_name='جدید'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, default='100.000', max_length=500, null=True, verbose_name='قیمت'),
        ),
    ]
