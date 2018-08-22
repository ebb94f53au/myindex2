from django.db import models

# Create your models here.
class aboutInfo(models.Model):
    img=models.ImageField(upload_to='images/about',verbose_name='图片★')
    text=models.TextField(verbose_name='关于详细★')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        verbose_name='关于页详细'
        verbose_name_plural='关于页详细'
