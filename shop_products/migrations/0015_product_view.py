# Generated by Django 3.1.5 on 2021-01-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0014_auto_20210122_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
