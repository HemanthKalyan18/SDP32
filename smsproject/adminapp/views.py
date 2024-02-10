from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin, User, Stock


def adminhome(request):
    return render(request, "adminhome.html")


def logout(request):
    return render(request, "index.html")


def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request, "adminhome.html")
    else:
        return HttpResponse("Login Failed")


def viewstocks(request):
    stocks = Stock.objects.all()
    return render(request, "viewstocks.html", {"stockdata": stocks})


def viewusers(request):
    users = User.objects.all()
    return render(request, "viewusers.html", {"userdata": users})


def adminstock(request):
    return render(request, "adminstock.html")


def adminuser(request):
    return render(request, "adminuser.html")


def addstocks(request):
    return render(request, "addstocks.html")


def insertstock(request):
    if request.method == "POST":
        ticker_symbol = request.POST["ticker_symbol"]
        company_name = request.POST["company_name"]
        market_capitalization = request.POST["market_capitalization"]
        dividend_yield = request.POST["dividend_yield"]
        beta = request.POST["beta"]
        week_52_high = request.POST["week_52_high"]
        week_52_low = request.POST["week_52_low"]

        stock = Stock(ticker_symbol=ticker_symbol, company_name=company_name,
                      market_capitalization=market_capitalization, dividend_yield=dividend_yield, beta=beta,
                      week_52_high=week_52_high, week_52_low=week_52_low)

        Stock.save(stock)
    return HttpResponse("Stock Added Successfully")


def deletestock(request):
    stocks = Stock.objects.all()
    return render(request, "deletestock.html", {"stockdata": stocks})


def stockdeletion(request):
    return HttpResponse("I am in Stock Deletion")


def deleteuser(request):
    users = User.objects.all()
    return render(request, "deleteuser.html", {"userdata": users})


def userdeletion(request):
    return HttpResponse("I am in User Deletion")

def adduser(request):
    return render(request, "adduser.html")

def insertuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        date_of_birth = request.POST["date_of_birth"]
        mobile_number = request.POST["mobile_number"]

        user = User(username=username, email=email,
                      password=password, date_of_birth=date_of_birth, mobile_number=mobile_number)

        User.save(user)
    return HttpResponse("User Added Successfully")

def vi(request):
    return render(request,"vi.html")

def eirfc(request):
    return render(request,"eirfc.html")

def tatasteel(request):
    return render(request,"tatasteel.html")

def zomato(request):
    return render(request,"zomato.html")
