from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse,HttpResponse
from django.views.generic.base import TemplateView,View
from .messageForm.Form import messageForm
# Create your views here.
from .models import Info,Message
from captcha.views import CaptchaStore,captcha_image_url
from django.core.mail import send_mail
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

        info=get_object_or_404(Info,isDelete=False)

        form= messageForm()
        return render(request,'contact.html',{'info':info,
                                              'title':'★联系页面',
                                              'form':form})
    def post(self,request):
        #post时提交联系信息
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()
            email_info='姓名：'+message.name+'\n'+'联系方式：'+message.phone+'\n'+'邮箱：'+message.email+'\n'+'留言：'+message.message

            return JsonResponse({'status': 'success',
                                 'email_info':email_info})

        else:
            message = request.POST.get('message')
            print(type(message))
            return JsonResponse({'status': 'error',
                                 'message':message})


from django.conf import  settings
def send_email(request):
    if request.method=='POST':
        email_info=request.POST.get('email_info')
        print(email_info)
        # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，
        # 收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)

        if email_info:
            #settings.EMAIL_HOST_USER,settings.EMAIL_INTO_LIST 在setting 中定义
            send_mail('您收到一封来自www.siyang.site的留言', email_info, settings.EMAIL_HOST_USER,settings.EMAIL_INTO_LIST ,
                      fail_silently=False)
        else:
            return JsonResponse({'status': 'error'})
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error'})