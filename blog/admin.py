from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author','isDelete']
    class Media:
        js = (
            "js/jquery.min.js",
            "tinymce/js/tinymce/jquery.tinymce.min.js",
            "tinymce/js/tinymce/tinymce.min.js",
            "tinymce/js/tinymce/textareas.js",

        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','isDelete']
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','isDelete']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','text','created_time','post','isDelete']

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)
