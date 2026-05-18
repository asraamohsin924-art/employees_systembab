from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass