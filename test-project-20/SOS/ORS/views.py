from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .ctl.UserCtl import UserCtl
from .ctl.RoleCtl import RoleCtl


@csrf_exempt
def action(request, page="", operation="", id=0):
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    res = ctlObj.execute(request, {"operation": operation, "id": id})
    return res


def index(request):
    res = render(request, 'Welcome.html')
    return res


from django.shortcuts import render

# Create your views here.
