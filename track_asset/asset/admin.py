from django.contrib import admin
from .models import (Company,Employee,Device)
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','phonenumber',]
admin.site.register(Company,CompanyAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['user','company']
admin.site.register(Employee,EmployeeAdmin)
class DeviceAdmin(admin.ModelAdmin):
    list_display=['device_name','desc','condition']
admin.site.register(Device,DeviceAdmin)