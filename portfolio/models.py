from django.db import models

# Create your models here.
import os
from django .conf import settings


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

    def add_downloadNum(self):
        self.downloadNum+=1
        self.save()
import  django.utils.timezone as timezone
class Resources(models.Model):
    name =models.CharField(max_length=100,verbose_name='资源名字★')
    time =models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    project=models.FileField(default='upload/portfolio/file/null',upload_to='upload/portfolio/file',verbose_name='资源地址*')
    downloadNum=models.IntegerField(verbose_name='下载量',default=0)
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        ordering=['name']
        verbose_name='分享资源'
        verbose_name_plural='分享资源'
    def add_downloadNum(self):
        self.downloadNum+=1
        self.save()


from django.dispatch import receiver
from django.db.models.signals import post_delete
@receiver(post_delete, sender=Resources)
@receiver(post_delete, sender=Portfolio)
def delete_upload_files(sender, instance, **kwargs):
    # xadmin 删除自动删除本地文件
    files = getattr(instance, 'project', '')
    if not files:
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)
    if isinstance(instance,Portfolio):
        files = getattr(instance, 'img', '')
        if not files or files.name=='upload/portfolio/poster/img-1.jpg':
            return
        fname = os.path.join(settings.MEDIA_ROOT, str(files))
        if os.path.isfile(fname):
            os.remove(fname)
