# Generated by Django 3.1.5 on 2021-01-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0021_auto_20210124_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='posting_details',
            field=models.CharField(default='', max_length=500, verbose_name='جزئیات ارسال'),
        ),
    ]
