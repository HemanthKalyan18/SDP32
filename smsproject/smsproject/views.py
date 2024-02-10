from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return render(request,"initial.html")


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")


def contactus(request):
    return render(request, "contact.html")

