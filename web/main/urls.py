from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from register import views as v
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
path("", views.index, name="index"),
path("index", views.index, name="index"),
path('mypage', views.mypage, name='mypage'),
path('expert', views.expert, name='expert'),
] 