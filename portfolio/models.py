from django.db import models

# Create your models here.

class Portfolio(models.Model):
    #个人作品展示
    name=models.CharField(max_length=100,verbose_name='项目名字★')
    img=models.ImageField(default='upload/portfolio/poster/img-1.jpg',upload_to='upload/portfolio/poster',verbose_name='封面海报')
    info=models.CharField(max_length=255,verbose_name='概述★')
    url=models.CharField(max_length=255,verbose_name='项目网址★')
    project=models.FileField(default='upload/portfolio/file/null',upload_to='upload/portfolio/file',verbose_name='项目*')
    downloadNum=models.IntegerField(verbose_name='下载量',default=0)
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')

    class Meta:
        ordering=['name']
        verbose_name='个人作品'
        verbose_name_plural='个人作品'

