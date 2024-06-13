from django.shortcuts import render
from django.http import HttpResponse

def print_hello(request):

    movie_details = {
        'title':'Godfather',
        'year' : 1990,
        'summary':'Story of an underworld King'
    }
    return render(request,'hello.html',movie_details)
