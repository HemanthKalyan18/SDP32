from django.urls import path
from . import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),

    path("viewstocks", views.viewstocks, name="viewstocks"),
    path("viewusers", views.viewusers, name="viewusers"),

    path("adminstock",views.adminstock,name="adminstock"),
    path("adminuser",views.adminuser,name="adminuser"),

    path("addstocks", views.addstocks, name="addstocks"),
    path("insertstock", views.insertstock, name="insertstock"),
    path("deletestock", views.deletestock, name="deletestock"),
    path("stockdeletion", views.stockdeletion, name="stockdeletion"),

    path("adduser", views.adduser, name="adduser"),
    path("insertuser", views.insertuser, name="insertuser"),
    path("deleteuser", views.deleteuser, name="deleteuser"),
    path("userdeletion", views.userdeletion, name="userdeletion"),

    path("vi", views.vi, name="vi"),
    path("eirfc", views.eirfc, name="eirfc"),
    path("tatasteel", views.tatasteel, name="tatasteel"),
    path("zomato", views.zomato, name="zomato"),

]
