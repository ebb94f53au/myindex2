from django.contrib import admin
from django.urls import path,include
from .views import *


app_name='portfolio'
urlpatterns = [

    path('portfolio/',PortfolioView.as_view(),name='portfolio_get'),
    path('download/<int:pk>/',Download,name='download')


]
