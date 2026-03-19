from django.http import HttpResponse
from django.shortcuts import render


def test_crud(request):
    return HttpResponse("<h1> Hii I am your crud app page")


def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    return render(request,"registration.html")

def signin(request):
    return render(request,"login.html")
