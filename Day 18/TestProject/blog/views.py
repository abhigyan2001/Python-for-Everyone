from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'C:\\Users\\Abhigyan\\OneDrive\\Documents\\GitHub\\Python-for-Everyone\\Day 18\\TestProject\\blog\\templates'],
        'APP_DIRS': True
        ,
    },
]

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blogs Home</h1>")

def about(request):
    author = "Abhigyan"
    title = "About"
    html = render_to_string("about.html", {'title': title, 'author': author})
    return HttpResponse(html)