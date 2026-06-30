from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, EmployeeInfo
from .resources import EmployeeResource, EmployeeInfoResource


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    
@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(ImportExportModelAdmin):
    resource_class = EmployeeInfoResource