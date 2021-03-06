from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
import django.utils.timezone as timezone
# Create your models here.
class Category(models.Model):
    #分类
    name = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    def __str__(self):
        return self.name
    class Meta:

        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'


class Tag(models.Model):
    #标签
    name = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='博客标签'
        verbose_name_plural='博客标签'


from DjangoUeditor.models import UEditorField
class Post(models.Model):
    #博客
    title = models.CharField(max_length=70,verbose_name='文章标题★')
    body = UEditorField(verbose_name='文章正文★',height=300, width=800,max_length=1024000000000,
                           default=u'', blank=True, imagePath='upload/blog/context',
                           toolbars='besttome', filePath='upload/blog/context')
    #正文中有图片信息在images/blog/conImg文件夹中
    created_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    modified_time = models.DateTimeField(default=timezone.now,verbose_name='修改时间★')
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='文章摘要')
    views = models.PositiveIntegerField(default=0,verbose_name='阅读量')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类★')
    tags = models.ManyToManyField(Tag, blank=True,verbose_name='标签★')
    img = models.ImageField(default='upload/blog/poster/img-4.jpg',upload_to='upload/blog/poster',verbose_name='图片')#MEDIA
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，
    # User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    def get_absolute_url(self):
        return reverse('blog:blogDetail_get', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客内容'
        verbose_name_plural = '博客内容'

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:20]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    #评论
    name = models.CharField(max_length=100,verbose_name='名字★')
    email = models.EmailField(max_length=255,verbose_name='邮箱★')
    text = models.TextField(verbose_name='评论正文★')
    created_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')

    post = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name='博客★')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客评论'
        verbose_name_plural = '博客评论'
    def __str__(self):
        return self.text[:20]

class CommentBack(models.Model):
    #评论的回复，暂时只能博主回复
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,verbose_name='评论★')
    text = models.TextField(verbose_name='评论回复正文★')
    created_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')

    class Meta:
        ordering = ['created_time']
        verbose_name = '博客评论回复'
        verbose_name_plural = '博客评论回复'
    def __str__(self):
        return self.text[:20]

from django.dispatch import receiver
from django.db.models.signals import post_delete,post_save
from django.conf import settings
import os
import re
@receiver(post_delete, sender=Post)
def delete_upload_files(sender, instance, **kwargs):
    # xadmin 删除自动删除本地文件
    files = getattr(instance, 'img', '')
    if not files or files.name=='upload/blog/poster/img-4.jpg':
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)
    body =getattr(instance, 'body', '')
    # b = re.findall(r'<img src="/static/media/(.+?)"(?:.+?)/>',str(body))
    b = re.findall(r'"/static/media/(.+?)"',str(body))
    for i in b:
        fname = os.path.join(settings.MEDIA_ROOT, str(i))
        if os.path.isfile(fname):
            os.remove(fname)


from django.core.mail import send_mail
@receiver(post_save, sender=CommentBack)
def save_commentBack(sender, instance, **kwargs):
    #留言回复，邮件提醒
    text=getattr(instance,'text','')
    email=[instance.comment.email]
    postname=instance.comment.post.title
    comment_text=instance.comment.text
    pk=instance.comment.post.pk
    email_info='您好，我是司杨个人网站(www.siyang.site)的管理员' \
               '，首先感谢您在博客【'+postname+'】(www.siyang.site/blog/'+str(pk)+'/)的留言，' \
                 '根据此留言:\n【'+comment_text+'】\n在此做出回复:\n【'+text+'】\n最后感谢您的支持,祝您生活愉快。'
    send_mail('您收到一封来自www.siyang.site的留言回复', email_info, settings.EMAIL_HOST_USER, [instance.comment.email],
              fail_silently=False)
