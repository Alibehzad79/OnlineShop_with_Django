# Generated by Django 3.1.5 on 2021-01-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0013_auto_20210122_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_type',
            field=models.CharField(choices=[('جدید', 'بله'), (' ', 'خیر')], default=' ', max_length=200, verbose_name='جدید'),
        ),
    ]
