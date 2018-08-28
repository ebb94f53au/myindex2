from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import aboutInfo
import markdown

from markdown.extensions.toc import TocExtension
# Create your views here.
class AboutPageView(TemplateView):
    #关于页展示
    template_name='about.html'
    def get_context_data(self, **kwargs):
        context=super(AboutPageView,self).get_context_data(**kwargs)
        try:
            info=aboutInfo.objects.get(isDelete=False)
            info.text=markdown.markdown(info.text,extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
            context['info']=info
        except:
            pass
        context['title']='关于本站'
        return context