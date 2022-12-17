from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Users

# Create your views here.
def index(request):
    return render(request,'sql_demo/pages/home.html',{
        'page':'main'
    })


def solution1(request):
    return render(request,'sql_demo/pages/solution1.html',{
        'page':'solution1'
    })
    # return HttpResponse("solution1")

def solution2(request):
    return render(request,'sql_demo/pages/solution2.html',{
        'page':'solution2'
    })
    # return HttpResponse("solution2")

def solution3(request):
    return render(request,'sql_demo/pages/solution3.html',{
        'page':'solution3'
    })


def fault_system(request):
    cursor=connection.cursor()
    cursor.execute("select * from sql_demo_users where email='"+request.POST.get('email')+"' and password='"+request.POST.get('password')+"'")
    return HttpResponse(cursor.fetchall())

def solution_one(request):
    user=Users.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
    # print(user)
    return HttpResponse("User logged in successfull,Welcome "+user.email)

def solution_two(request):
    user=Users.objects.raw('SELECT * FROM sql_demo_users WHERE email=%s and password=%s',[request.POST.get('email'),request.POST.get('password')])
    return HttpResponse("User logged in successfull,Welcome "+user[0].email)