from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from django.views.generic.base import TemplateView,View
from .messageForm.Form import messageForm
# Create your views here.
from .models import Info,Message
class ContactPageView(View):
    #联系页面
    def get(self,request):
        #get时展示联系方式
        info=get_object_or_404(Info, isDelete=False)
        return render(request,'contact.html',{'info':info,
                                              'title':'★联系页面'})
    def post(self,request):
        #post时提交联系信息
        form = messageForm(request.POST)
        print('11111111'*22)
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
