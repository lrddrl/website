from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
from django.core.files.base import ContentFile
from . models import mypicture

import os


# Create your views here.

from django.core.files.base import ContentFile

def index(response):
	return render(response, "index.html", {})

def home(response):
	return render(response, "home.html", {})

def contact(response):
	return render(response, "contact.html", {})

def industry(response):
	return render(response, "industry.html", {})

def teams(response):
	return render(response, "teams.html", {})

def token(response):
	return render(response, "token.html", {})

def market(response):
	return render(response, "market.html", {})
	
def mypage(response):
    return redirect('/show1/')
	#return render(response, "page.html", {})

def expert(response):
    return redirect('/show2/')
	#return render(response, "expert.html", {})

def showing1(request):
    imgs = models.mypicture.objects.all() # 
    # 
    content = {
        'imgs': imgs
    }
    # 
    for i in imgs:
        # 
        print(i.photo)
    # 
    return render(request, 'mypage.html', content)


def showing2(request):
    imgs = models.mypicture.objects.all() # 
    # 
    content = {
        'imgs': imgs
    }
    # 
    for i in imgs:
        # 
        print(i.photo)
    # 
    return render(request, 'expert.html', content)


def updateE(request):
    if request.method == 'POST':
        # img = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        expert = models.Expert(
            E_fname    = request.POST.get("firstname"),
            E_lname    = request.POST.get("lastname"),    
            E_phone    = request.POST.get("phone"),     
        )

        expert.save()  # 
        return HttpResponse('upload successful！')  

    return render(request, 'mypage.html')    

def updateinfo(request):
    if request.method == 'POST':
        new_img = mypicture(
            photo=request.FILES.get('photo'),  # 
            user=request.FILES.get('photo').name # 
        )
        new_img.save()  # 
        #return HttpResponse('Upload successful！')  
        return redirect('/show/')

    return render(request, 'mypage.html')

