from django.contrib import admin
from .models import *
# Register your models here.
class WheelAdmin(admin.ModelAdmin):
    list_display = ['text','img','isDelete']
class ViewsNumAdmin(admin.ModelAdmin):
    list_display = ['todayNum','date','sumNum','isDelete']
admin.site.register(Wheel,WheelAdmin)
admin.site.register(ViewsNum,ViewsNumAdmin)