from django.shortcuts import render
from django.http import HttpResponse

def print_hello(request):

    movie_details ={ 
        'movie' : [{
        'title':'Godfather',
        'year' : 1990,
        'summary':'Story of an underworld King',
        'success' : False,
    },
    {   
        'title':'Godfather',
        'year' : 1990,
        'summary':'Story of an underworld King',
        'success' : False, 
    },
    {
        'title':'Godfather',
        'year' : 1990,
        'summary':'Story of an underworld King',
        'success' : False,
    },
    ]}
    return render(request,'hello.html',movie_details)
