# Generated by Django 3.1.5 on 2021-01-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogform',
            name='blog_title',
            field=models.CharField(default='', max_length=200000, verbose_name='عنوان'),
        ),
    ]
