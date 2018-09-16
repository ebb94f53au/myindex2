from django.contrib import admin
from django.urls import path,include
from .views import AboutPageView
from django.views.decorators.cache import cache_page


app_name='about'
urlpatterns = [

    path('about/',cache_page(60*60)(AboutPageView.as_view()),name='about_get'),

]