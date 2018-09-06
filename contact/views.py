from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse,HttpResponse
from django.views.generic.base import TemplateView,View
from .messageForm.Form import messageForm
# Create your views here.
from .models import Info,Message
from captcha.views import CaptchaStore,captcha_image_url
class ContactPageView(View):
    #联系页面
    def get(self,request):
        #刷新验证码
        if request.GET.get('newsn') == '1':
            # 生成的数字
            csn = CaptchaStore.generate_key()
            #生成的图片路径
            cimageurl = captcha_image_url(csn)

            return HttpResponse(cimageurl)

        # get时展示联系方式
        try:
            info=Info.objects.get(isDelete=False)
        except:
            pass
        register_from= messageForm()
        return render(request,'contact.html',{'info':info,
                                              'title':'★联系页面',
                                              'register_from':register_from})
    def post(self,request):
        #post时提交联系信息
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()
            return JsonResponse({'status': 'success'})

        else:
            return JsonResponse({'status': 'error'})

# def create_message(request):
#     if request.method=='POST':
#         form=messageForm(request.POST)
#
#         if form.is_valid():
#             message=form.save()
#             message.save()
#             return JsonResponse({'status':111})
#         else:
#             return redirect('/contact/')
#     else:
#         return redirect('/contact/')
