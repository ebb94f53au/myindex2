"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import xadmin
xadmin.autodiscover()
from  django.conf.urls import handler404,handler500
from .views import to_404page,to_500page

handler404 = to_404page
handler500 = to_500page

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', xadmin.site.urls),
    path('',include('home.urls')),
    path('',include('about.urls')),
    path('',include('blog.urls')),
    path('',include('contact.urls')),
    path('',include('portfolio.urls')),
    path('ueditor/',include('DjangoUeditor.urls' )),
    path('captcha/', include('captcha.urls')),




]
