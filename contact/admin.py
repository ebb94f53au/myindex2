from django.contrib import admin
from .models import Info,Message
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ['email','wechat','phone','isDelete']
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message','datetime','isDelete']
admin.site.register(Info,InfoAdmin)
admin.site.register(Message,MessageAdmin)