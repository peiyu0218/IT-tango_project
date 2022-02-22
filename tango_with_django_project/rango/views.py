from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    res = HttpResponse("Rango says hey there partner!!")
    res.write("<a href='/rango/about/'>About</a>")
    return res
def about(request):
    res = HttpResponse("Rango says here is the about page.")
    res.write("<a href='/rango/'>Index</a>")
    return res
