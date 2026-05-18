from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee
from .resources import EmployeeResource


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource