import xadmin
from .models import *
# Register your models here.
class AboutInfoAdmin(object):
    list_display = ['text','img','isDelete']
    search_fields = ['text','img','isDelete']
    list_filter = ['text','img','isDelete']

    #富文本
    style_fields = {"text": "ueditor"}
xadmin.site.register(aboutInfo,AboutInfoAdmin)