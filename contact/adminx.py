import xadmin
from .models import Info,Message
# Register your models here.
class InfoAdmin(object):
    list_display = ['email','wechat','phone','isDelete']
    search_fields = ['email','wechat','phone','isDelete']
    list_filter = ['email','wechat','phone','isDelete']
class MessageAdmin(object):
    list_display = ['name','email','phone','message','datetime','isDelete']
    search_fields = ['name','email','phone','message','datetime','isDelete']
    list_filter = ['name','email','phone','message','datetime','isDelete']
xadmin.site.register(Info,InfoAdmin)
xadmin.site.register(Message,MessageAdmin)