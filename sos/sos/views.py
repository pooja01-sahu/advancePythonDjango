from django.http import HttpResponse


def test_sos(request):
    return HttpResponse("<h1>Hi my first project of django</h1>")