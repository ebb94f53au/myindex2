from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.decorators.cache import cache_page

app_name='portfolio'
urlpatterns = [

    path('portfolio/',PortfolioView.as_view(),name='portfolio_get'),
    path('download/<int:type>/<int:pk>/',Download,name='download')


]
