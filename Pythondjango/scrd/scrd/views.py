from django.http import HttpResponse
from django.shortcuts import render


def test_scrd(request):
    return HttpResponse("<h1>Hi am your scrd first file</h1>")
