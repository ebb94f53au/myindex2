from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView
from .models import Wheel,ViewsNum
from blog.models import Post
import datetime
# Create your views here.
class HomePageView(TemplateView):
    #主页类视图
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        #主页浏览量增加，没有今天的创建
        response=super(HomePageView,self).get(request, *args, **kwargs)
        today = datetime.date.today()

        try:
            num=ViewsNum.objects.get(date=today,isDelete=False)
            num.addToday()
            num.addSum()
        except:
            try:
                nums=ViewsNum.objects.filter(isDelete=False)[0].sumNum
            except:
                nums=1
            ViewsNum.create(today,nums)
        return response

    def get_context_data(self, **kwargs):
        #滚动画面 推荐博客
        context=super(HomePageView,self).get_context_data(**kwargs)
        today = datetime.date.today()
        context['wheels']=Wheel.objects.filter(isDelete=False)
        context['post_list'] = Post.objects.filter(isDelete=False)[:4]
        context['title'] = '司杨的个人主页'

        try:
            context['viewsNums']=ViewsNum.objects.get(date=today,isDelete=False)
        except:
            pass
        # context['viewsNums']=get_object_or_404(ViewsNum,date=today,isDelete=False)

        return context