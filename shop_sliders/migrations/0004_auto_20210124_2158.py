# Generated by Django 3.1.5 on 2021-01-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_sliders', '0003_auto_20210124_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='sliders', verbose_name='تصویر'),
        ),
    ]
