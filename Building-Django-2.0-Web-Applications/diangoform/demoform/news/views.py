from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.


def index(request):
    return HttpResponse('xin chao')

def add_post(request):
    a = PostForm()
    return render(request,'',{'f': a})