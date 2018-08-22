from django.contrib import admin
from .models import *
# Register your models here.
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ['text','img','isDelete']
    class Media:
        js = (
            "js/jquery.min.js",
            "tinymce/js/tinymce/jquery.tinymce.min.js",
            "tinymce/js/tinymce/tinymce.min.js",
            "tinymce/js/tinymce/textareas.js",

        )

admin.site.register(aboutInfo,AboutInfoAdmin)