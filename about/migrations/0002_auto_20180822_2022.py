# Generated by Django 2.0.7 on 2018-08-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinfo',
            name='img',
            field=models.ImageField(upload_to='images/about', verbose_name='图片★'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='text',
            field=models.TextField(verbose_name='关于详细★'),
        ),
    ]