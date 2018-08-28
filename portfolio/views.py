from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.generic import ListView
# Create your views here.
from .models import Portfolio
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
        context['title']='司杨的个人作品'

        return context

import os
from django.conf import settings
def Download(request,pk):
    #下载个人作品源码
    p=Portfolio.objects.get(pk=pk)
    path=os.path.join(settings.MEDIA_ROOT,p.project.name)
    def readFile(filename,size=512):
        with open(filename,'rb') as  f:
            while True:
                c=f.read(size)
                if c:
                    yield c
                else:
                    break
    response=StreamingHttpResponse(readFile(path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(p.project.name.split('/')[-1])

    return response
