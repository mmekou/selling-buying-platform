# Generated by Django 3.1 on 2021-01-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210111_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]
