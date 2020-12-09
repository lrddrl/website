from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('login/', views.logins),
    path('regist/', views.regist),
    path('logout/', views.log_out), 
] 