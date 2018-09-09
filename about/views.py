from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView
from .models import aboutInfo
# import markdown
#
# from markdown.extensions.toc import TocExtension
# Create your views here.
class AboutPageView(TemplateView):
    #关于页展示
    template_name='about.html'
    def get_context_data(self, **kwargs):
        context=super(AboutPageView,self).get_context_data(**kwargs)

        info=get_object_or_404(aboutInfo,isDelete=False)

        context['info']=info

        context['title']='关于本站'
        return context