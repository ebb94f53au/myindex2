from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.generic import ListView,DetailView
from django.views.generic import View
from .models import *
from .commentForm.Form import commentForm
# Create your views here.

class BlogPageView(ListView):
    #博客列表
    model = Post
    template_name = 'blog.html'
    context_object_name = 'post_list'
    paginate_by = 4
    def get_queryset(self):
        #选取没有逻辑删除的数据
        return Post.objects.filter(isDelete=False)
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(BlogPageView,self).get_context_data(**kwargs)

        context['title']='司杨的博客'

        return context
from django.core.paginator import Paginator
from captcha.views import CaptchaStore,captcha_image_url
class BlogDetailView(DetailView):
    #博客博文详细
    template_name = 'detail.html'
    model = Post
    def get(self, request, *args, **kwargs):
        #验证码
        if request.GET.get('newsn') == '1':
            # 生成的数字
            csn = CaptchaStore.generate_key()
            #生成的图片路径
            cimageurl = captcha_image_url(csn)

            return HttpResponse(cimageurl)


        response=super(BlogDetailView,self).get(request, *args, **kwargs)
        # 每看一次阅读数数量加一
        self.object.increase_views()

        return response
    def get_object(self, queryset=None):
        #自动找到哪篇博客根据urls ：pk
        post=super(BlogDetailView,self).get_object()
        post.body=markdown.markdown(post.body,extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
        return post
    def get_context_data(self, **kwargs):
        #分页评论数据
        context=super(BlogDetailView,self).get_context_data(**kwargs)
        page_by = 10

        paginator = Paginator(self.object.comment_set.all(), page_by)

        pageNum=self.request.GET.get('page') if  self.request.GET.get('page') else 1
        #当pagenum不存在时为1
        pageNum=pageNum if int(pageNum) <= paginator.num_pages else 1
        # 当pagenum大于总数是为1

        comments = paginator.page(pageNum)
        context['comments'] = comments
        context['paginator'] = paginator
        context['is_paginated'] = True
        context['title'] = self.object.title
        form = commentForm()
        context['form']=form
        if paginator.num_pages==0 or paginator.num_pages==1:
            context['is_paginated'] = False
        return context


class CommentPost(View):
    #评论提交
    def post(self,request):
        form = commentForm(request.POST)

        if form.is_valid():
            comment = form.save()
            comment.save()
            return JsonResponse({'status': 'success'})

        else:
            return JsonResponse({'status': 'error'})

# import os
# from django.conf import settings
# import time
# def uploadIMG(request):
#     #admin后台富文本上传图片
#     if request.method == 'POST':
#         img = request.FILES.get('img')
#         if img.name.split('.')[1]=='jpg' or img.name.split('.')[1]=='png' or img.name.split('.')[1]=='jpeg'\
#             or img.name.split('.')[1]=='bmp':
#             imgName=str(time.time())+'.'+img.name.split('.')[1]
#             filepath = os.path.join(settings.MEDIA_ROOT+'upload/blog/context',imgName )
#             with open(filepath, 'wb') as sc:
#                 for info in img.chunks():
#                     sc.write(info)
#
#             return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox')."
#                                 "val('/static/media/upload/blog/context/"+imgName+"').closest('.mce-window').find('.mce-primary').click();</script>")
#         else:
#             return HttpResponse('上传失败')
#     else:
#         return HttpResponse('上传失败')

