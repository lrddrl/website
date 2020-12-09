from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path('mypage', views.mypage, name='mypage'),
    path('expert', views.expert, name='expert'),
    path('updateinfo/', views.updateinfo), 
    path('updateE/', views.updateE),
    path('show1/',views.showing1, name='photos'), 
    path('show2/',views.showing2, name='photos'), 

] 