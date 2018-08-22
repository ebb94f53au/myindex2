from django.contrib import admin
from .models import *
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','img','url','info','project','isDelete']
admin.site.register(Portfolio,PortfolioAdmin)