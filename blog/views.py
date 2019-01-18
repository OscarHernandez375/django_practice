from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Osqui',
        'title': 'Post1',
        'content': 'cmment1',
        'date_posted': '10/10/2010'
    },
    {
        'author': 'Osqui2',
        'title': 'Post2',
        'content': 'comment2',
        'date_posted': '11/10/2010'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
