from django.shortcuts import render,get_object_or_404,redirect
from django.http import StreamingHttpResponse,HttpResponseRedirect
from django.views.generic import ListView
# Create your views here.
from .models import Portfolio,Resources
class PortfolioView(ListView):
    #个人作品列表
    template_name = 'portfolio.html'
    model = Portfolio
    paginate_by = 4
    context_object_name = 'portfolio_list'
    def get_queryset(self):
        return Portfolio.objects.filter(isDelete=False)
    def get_context_data(self, **kwargs):
        context=super(PortfolioView,self).get_context_data(**kwargs)
        res=Resources.objects.filter(isDelete=False)
        context['title']='司杨的个人作品/资源'
        context['resources']=res
        return context

# import os
# from django.conf import settings
# def Download(request,pk):
#     #下载个人作品源码
#     p=get_object_or_404(Portfolio,pk=pk,isDelete=False)
#     path=os.path.join(settings.MEDIA_ROOT,p.project.name)
#     #判断是否存在文件
#     flag=os.path.exists(path)
#
#     def readFile(filename,size=512):
#         with open(filename,'rb') as  f:
#             while True:
#                 c=f.read(size)
#                 if c:
#                     yield c
#                 else:
#                     break
#
#     if flag:
#         p.add_downloadNum()
#         response=StreamingHttpResponse(readFile(path))
#         response['Content-Type'] = 'application/octet-stream'
#         response['Content-Disposition'] = 'attachment;filename="{0}"'.format(p.project.name.split('/')[-1])
#         return response
#     else:
#         return  render(request,'error/404.html',{'title':'页面没有找到'})

import os
from django.conf import settings
def Download(request,type,pk):
    #下载页面，0为个人作品下载，1为资源下载
    if type==0:
        type=Portfolio
    elif type == 1:
        type=Resources


    p = get_object_or_404(type, pk=pk, isDelete=False)
    path = os.path.join(settings.MEDIA_URL, p.project.name)
    p.add_downloadNum()
    return HttpResponseRedirect(path)