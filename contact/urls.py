from django.contrib import admin
from django.urls import path,include
from .views import *


app_name='contact'
urlpatterns = [

    path('contact/',ContactPageView.as_view(),name='contact_get'),
    path('contact/send_email/',send_email,name='send_email'),

]
