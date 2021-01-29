# Generated by Django 3.1.5 on 2021-01-28 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0030_auto_20210128_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgallery',
            name='product',
        ),
        migrations.AddField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_products.product', verbose_name='محصول'),
            preserve_default=False,
        ),
    ]
