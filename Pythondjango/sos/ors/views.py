from django.shortcuts import render, redirect
from django.http import HttpResponse

from .service.marksheet_service import Marksheet
from .service.user_service import UserService


def test_ors(request):
    return HttpResponse("<h1>Hi my first project of ors not sos</h1>")


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def signup_test(request):
    print(request.GET.get("firstName"))
    print(request.GET.get("lastName"))
    print(request.GET.get("email"))
    print(request.GET.get("dob"))
    print(request.GET.get("address"))
    return render(request, 'registration.html')


def user_signup_test(request):
    message = ""
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
        message = "User Registered Successfully..!!"
    return render(request, 'registration.html', {'message': message})


def login_test(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            loginId = request.POST.get("loginId")
            password = request.POST.get("password")
            service = UserService()
            user_data = service.auth(loginId,password)
            if len(user_data) != 0:
                request.session['firstName'] = user_data[0].get('firstName')
                return redirect('/')

                # return redirect('/')
                # return render(request,'welcome.html',{'firstName': user_data[0].get('firstName')})
            else:
                message = 'LoginId & Password invalid'
        if request.POST.get('operation') == "signUp":
            return redirect("/signup")
    print(request.POST.get('csrfmiddlewaretoken'))
    return render(request, 'login.html' , {'message': message})

def logout(request):
    request.session['firstName'] = None
    return redirect('/signin/')

def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "TestList.html", {"list": list})

def show_marksheet(request):
    message = ""
    if request.method == "POST":
        params = {}
        params['name'] = request.POST.get('name')
        params['rollno'] = request.POST.get('rollno')
        params['physics'] = request.POST.get('physics')
        params['chemistry'] = request.POST.get('chemistry')
        params['maths'] = request.POST.get('maths')
        service = Marksheet()
        service.add(params)
        message = "Add your marks Successfully..!!"
    return render(request, 'marksheet.html',{'message': message})

def add_user(request):
    return render(request, 'adduser.html')

def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, 'pageNo': params['pageNo'], 'index': index})
