# Generated by Django 3.1.5 on 2021-01-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_categories', '0001_initial'),
        ('shop_products', '0022_product_posting_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='shop_categories.Category', verbose_name='دسته بندی ها'),
        ),
    ]