from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

posts = [
    {
        'author': 'Frank',
        'title': 'Blog post 1',
        'content': 'First post content',
        'dete_posted': 'April 01,2024'
    },
     {
        'author': 'Yiga',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'dete_posted': 'April 02,2024'
    }
]


# Create your views here.
