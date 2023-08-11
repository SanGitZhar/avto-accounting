from django.contrib import admin
from .models import *


admin.site.register(Employee)
admin.site.register(Departments)
admin.site.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['model','user','avto_nomer','mileage']
    list_filter = ['model','user']
        