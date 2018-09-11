import xadmin
from .models import *
class PostAdmin(object):
    list_display = ['title', 'created_time', 'tags', 'modified_time', 'category', 'author','isDelete']
    # 列表显示
    search_fields = ['title', 'body']
    #查询字段
    list_filter = ['title', 'tags', 'category', 'author','isDelete']
    #过滤器

    style_fields = {"body": "ueditor"}


class CategoryAdmin(object):
    list_display = ['name','isDelete']
    search_fields = ['name','isDelete']
    list_filter = ['name','isDelete']


class TagAdmin(object):
    list_display = ['name','isDelete']
    search_fields = ['name','isDelete']
    list_filter = ['name','isDelete']


class CommentAdmin(object):
    list_display = ['name','email','text','created_time','post','isDelete']
    search_fields = ['name','isDelete']
    list_filter = ['name','email','text','created_time','post','isDelete']

class CommentBackAdmin(object):
    list_display = ['comment','text','created_time','isDelete']
    search_fields = ['name','isDelete']
    list_filter = ['comment','text','created_time','isDelete']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(CommentBack,CommentBackAdmin)
