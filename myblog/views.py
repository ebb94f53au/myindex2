from django.shortcuts import render

def to_404page(request, exception, template_name='error/404.html'):
    return render(request,template_name,{'title':'页面没有找到','error':exception})

def to_500page(request, template_name='error/500.html'):
    return render(request,template_name,{'title':'服务器错误'})