from django.contrib import admin
from django.urls import path
from .views import *


app_name='index'
urlpatterns = [

    path('',HomePageView.as_view(),name='get_index'),
    path('index/',HomePageView.as_view(),name='get_index'),


]
