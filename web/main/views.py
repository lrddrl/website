from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
	return render(response, "index.html", {})


def mypage(response):
	return render(response, "mypage.html", {})


def expert(response):
	return render(response, "expert.html", {})
