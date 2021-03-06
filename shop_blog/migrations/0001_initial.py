# Generated by Django 3.1.5 on 2021-01-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توصیحات')),
                ('author_name', models.CharField(max_length=200, verbose_name='نام نویسنده')),
                ('image', models.ImageField(upload_to='blog', verbose_name='تصویر')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')),
                ('is_published', models.BooleanField(default=False, verbose_name='منتشر شود / نشود')),
                ('blog_visit', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
            ],
            options={
                'verbose_name': 'بلاگ',
                'verbose_name_plural': 'بلاگ ها',
            },
        ),
        migrations.CreateModel(
            name='BlogForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('is_read', models.BooleanField(default=False, verbose_name='خوانده شده / نشده')),
            ],
            options={
                'verbose_name': 'نظرات',
                'verbose_name_plural': 'نطرات کاربران ',
            },
        ),
    ]
