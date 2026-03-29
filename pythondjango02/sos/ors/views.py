from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Marksheet


def welcome(request):
    return render(request, 'welcome.html')

def user_signup(request):
    message = ''
    if request.method == "POST":
        userName = request.POST["userName"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        obj = User.objects.create_superuser(userName, email, password)
        obj.first_name = firstName
        obj.last_name = lastName
        obj.save()
        message = 'User Registered Successfully'
    return render(request, "registration.html", {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            userName = request.POST["userName"]
            password = request.POST["password"]
            user = authenticate(username=userName, password=password)
            if user is not None:
                request.session["userName"] = userName
                login(request, user)
                return redirect('/ors/welcome/')
            else:
                message = 'Invalid User'
        if request.POST.get('operation') == "signUp":
            return redirect("/ors/signup/")
    return render(request, "login.html", {'message': message})


def user_logout(request):
    logout(request)
    return redirect('/ors/signin/')

def add_marksheet(request):
    message = ''
    if request.method == "POST":
        marksheet = Marksheet()
        marksheet.rollNo = request.POST["rollNo"]
        marksheet.name = request.POST["name"]
        marksheet.physics = request.POST["physics"]
        marksheet.chemistry = request.POST["chemistry"]
        marksheet.maths = request.POST["maths"]

        if request.POST['operation'] == "save":
            message = 'Marksheet Added Successfully'
        if request.POST['operation'] == "update":
            marksheet.id = int(request.POST.get('id', 0))
            message = 'Marksheet Updated Successfully'
        if request.POST['operation'] == "list":
            return redirect("/ors/list/")

        marksheet.save()
    return render(request, "marksheet.html", {'message': message})

def marksheet_list(request):
    list = Marksheet.objects.all()
    return render(request, "marksheetlist.html", {"list": list})

def delete_marksheet(request, id):
    obj = Marksheet.objects.get(id=id)
    obj.delete()
    return redirect("/ors/list/")

def edit_marksheet(request, id):
    message = ''
    obj = Marksheet.objects.get(id=id)
    return render(request, "marksheet.html", {"form": obj, "id": id, 'message': message})

def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")

def setCookies(request):
    key = "name"
    value = "abc"
    res = HttpResponse("<h1>cookie created..!!</h1>")
    res.set_cookie(key, value, max_age=20)
    return res


def getCookies(request):
    value = request.COOKIES.get('name')
    html = "<h3><center> value = {} </center></h3>".format(value)
    return HttpResponse(html)