from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>ok lets do it</h1>")

def about(request):
    return render(request,'blog/about.html')

def staticWeb(request):
    return render(request,'blog/staticWeb.html')