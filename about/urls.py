from django.contrib import admin
from django.urls import path,include
from .views import AboutPageView


app_name='about'
urlpatterns = [

    path('about/',AboutPageView.as_view(),name='about_get'),

]