# Generated by Django 3.1.5 on 2021-01-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='facebook', max_length=200)),
                ('link', models.URLField(verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'شبکه های اجتماعی',
            },
        ),
    ]