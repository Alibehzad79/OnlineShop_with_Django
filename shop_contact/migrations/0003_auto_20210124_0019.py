# Generated by Django 3.1.5 on 2021-01-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_contact', '0002_contact_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
    ]