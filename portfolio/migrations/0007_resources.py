# Generated by Django 2.0.7 on 2018-09-09 09:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_downloadnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='资源名字★')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('project', models.FileField(default='upload/portfolio/file/null', upload_to='upload/portfolio/file', verbose_name='资源地址*')),
                ('downloadNum', models.IntegerField(default=0, verbose_name='下载量')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
            options={
                'verbose_name': '分享资源',
                'verbose_name_plural': '分享资源',
                'ordering': ['name'],
            },
        ),
    ]