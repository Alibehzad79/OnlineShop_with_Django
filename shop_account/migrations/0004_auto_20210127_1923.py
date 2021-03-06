# Generated by Django 3.1.5 on 2021-01-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_account', '0003_auto_20210127_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpanel',
            name='address',
            field=models.TextField(blank=True, default='', null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='userpanel',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='users', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='userpanel',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='شماره تلفن'),
        ),
    ]
