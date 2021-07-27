from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.write("<p>Rango says hey there partner!</p>")
    response.write("<a href='/rango/about/'>About</a>")
    return response

def about(request):
    response = HttpResponse()
    response.write("<p>Rango says here is the about page.</p>")
    response.write("<a href='/rango/'>Index</a>")
    return response
