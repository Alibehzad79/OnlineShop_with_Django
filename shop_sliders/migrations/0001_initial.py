# Generated by Django 3.1.5 on 2021-01-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات کوتاه')),
                ('link', models.URLField(verbose_name='لینک')),
                ('image', models.ImageField(upload_to='sliders', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'اسلاید',
                'verbose_name_plural': 'اسلاید ها',
            },
        ),
    ]