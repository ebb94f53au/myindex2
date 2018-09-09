import xadmin
from .models import *
# Register your models here.
class PortfolioAdmin(object):
    list_display = ['name','img','url','info','project','downloadNum','isDelete']
    search_fields = ['name','img','url','info','project','downloadNum','isDelete']
    list_filter = ['name','img','url','info','project','downloadNum','isDelete']


class ResourcesAdmin(object):
    list_display = ['name','time','project','downloadNum','isDelete']
    search_fields = ['name','time','project','downloadNum','isDelete']
    list_filter = ['name','time','project','downloadNum','isDelete']
xadmin.site.register(Portfolio,PortfolioAdmin)
xadmin.site.register(Resources,ResourcesAdmin)