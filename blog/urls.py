from django.contrib import admin
from django.urls import path,include
from .views import *


app_name='blog'
urlpatterns = [

    path('blog/',BlogPageView.as_view(),name='blog_get'),
    path('blog/category/<int:pk>/',BlogPageViewByCategory.as_view(),name='blog_category_get'),
    path('blog/tag/<int:pk>/',BlogPageViewByTag.as_view(),name='blog_tag_get'),
    path('blog/<int:pk>/',BlogDetailView.as_view(),name='blogDetail_get'),
    path('blog/comment/',CommentPost.as_view(),name='commentPost'),
    # path('blog/uploadIMG/',uploadIMG,name='uploadIMG'),


]
