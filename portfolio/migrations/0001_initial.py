# Generated by Django 2.0.7 on 2018-08-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='项目名字')),
                ('img', models.ImageField(upload_to='', verbose_name='封面海报')),
                ('info', models.CharField(max_length=255, verbose_name='概述')),
                ('url', models.CharField(max_length=255, verbose_name='项目网址')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
            options={
                'verbose_name': '个人作品',
                'verbose_name_plural': '个人作品',
            },
        ),
    ]