from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Info(models.Model):
    #个人信息相关
    email=models.CharField(max_length=255,verbose_name='邮箱★')
    wechat=models.CharField(max_length=255,verbose_name='微信★')
    phone=models.CharField(max_length=255,verbose_name='手机号★')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        verbose_name='个人信息'
        verbose_name_plural='个人信息'
class Message(models.Model):
    name=models.CharField(max_length=100,verbose_name='姓名★')
    email=models.EmailField(max_length=255,verbose_name='邮箱★')
    phone=models.CharField(max_length=100,verbose_name='手机号★')
    message=models.TextField(verbose_name='留言★',null=False)
    datetime=models.DateTimeField(default=timezone.now,verbose_name='留言时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        verbose_name='留言信息'
        verbose_name_plural='留言信息'
    @classmethod
    def create(cls,name,email,phone,message):
        mes=cls(name=name,email=email,phone=phone,Message=message)
        mes.save()