# Generated by Django 3.1.5 on 2021-01-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_order', '0005_auto_20210125_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
