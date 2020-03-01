from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.

def index(repuest):
    return HttpResponse('hello')

def add_post(request):
    a = PostForm()
    return render(request,'news/',{'f' : a})

def save_news(request):
    if request.method=='POST':
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return  HttpResponse('luu ok')
        else:
            return HttpResponse('sai validate')
    else:
        return HttpResponse('khong phai post request')
