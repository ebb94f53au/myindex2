import xadmin
from .models import *
# Register your models here.
class WheelAdmin(object):
    list_display = ['text','img','isDelete']
    search_fields = ['text','img','isDelete']
    list_filter = ['text','img','isDelete']
class ViewsNumAdmin(object):
    list_display = ['todayNum','date','sumNum','isDelete']
    search_fields = ['todayNum','date','sumNum','isDelete']
    list_filter = ['todayNum','date','sumNum','isDelete']
from xadmin import views
#系统基础
class GlobalSetting(object):
    site_title = '司杨的个人网站'  # 设置头标题
    site_footer = '司杨的个人网站'  # 设置脚标题
    menu_style = 'accordion'
class BaseSetting(object):

    enable_themes =True

    use_bootswatch =True



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(Wheel,WheelAdmin)
xadmin.site.register(ViewsNum,ViewsNumAdmin)