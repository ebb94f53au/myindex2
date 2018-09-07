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
    img = models.ImageField(default='upload/blog/img-4.jpg',upload_to='upload/blog/poster',verbose_name='图片')#MEDIA
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，
    # User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'pk': self.pk})

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
