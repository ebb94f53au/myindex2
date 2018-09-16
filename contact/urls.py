from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.decorators.cache import cache_page


app_name='contact'
urlpatterns = [

    path('contact/',cache_page(60*60)(ContactPageView.as_view()),name='contact_get'),
    path('contact/send_email/',send_email,name='send_email'),

]
