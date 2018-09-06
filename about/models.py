from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class aboutInfo(models.Model):
    img=models.ImageField(upload_to='upload/about',verbose_name='图片★')
    text=UEditorField(verbose_name='关于详细★',height=300, width=800,max_length=1024000000000,
                           default=u'', blank=True, imagePath='upload/about',
                           toolbars='besttome', filePath='upload/about')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')
    class Meta:
        verbose_name='关于页详细'
        verbose_name_plural='关于页详细'
