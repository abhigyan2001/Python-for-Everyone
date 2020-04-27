from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1><br><p>This page is under construction</p>")

def about(request):
    return HttpResponse("<h1>About Page</h1><br><p>This page is under construction</p>")