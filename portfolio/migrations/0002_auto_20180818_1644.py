# Generated by Django 2.0.7 on 2018-08-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project',
            field=models.FileField(default='upload/portfolio/file/null', upload_to='upload/portfolio/file', verbose_name='项目'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(default='upload/portfolio/poster/img-1.jpg', upload_to='upload/portfolio/poster', verbose_name='封面海报'),
        ),
    ]
