from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('adminapp/', admin.site.urls),
    path("", views.demofunction, name="demo"),
    path("demo", views.demofunction, name="demo"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
    path("contact", views.contactus, name="contact"),

    path("", include("adminapp.urls")),
#    path("", include("user.urls")),

]
