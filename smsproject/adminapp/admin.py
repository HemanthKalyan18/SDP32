from django.contrib import admin
from .models import Admin,User,Stock

# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Stock)