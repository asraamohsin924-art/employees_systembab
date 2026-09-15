from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Employee, EmployeeInfo,
    Contract1000, ContractBachelorDiploma, ContractSecondary, Wage,
)
from .resources import (
    EmployeeResource, EmployeeInfoResource,
    Contract1000Resource, ContractBachelorDiplomaResource, ContractSecondaryResource, WageResource,
)


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ("emp_id", "name", "job_title", "grade", "stage", "base_salary")
    search_fields = ("emp_id", "name")


@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(ImportExportModelAdmin):
    resource_class = EmployeeInfoResource
    list_display = ("emp_id", "full_name", "job_title", "education", "grade", "stage")
    search_fields = ("emp_id", "full_name")


class ContractCategoryAdmin(ImportExportModelAdmin):
    list_display = ("code", "name", "job_title", "monthly_salary", "bank", "workplace")
    search_fields = ("code", "name", "phone", "workplace")
    ordering = ("name",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(category=self.contract_category)

    def save_model(self, request, obj, form, change):
        obj.category = self.contract_category
        super().save_model(request, obj, form, change)


@admin.register(Contract1000)
class Contract1000Admin(ContractCategoryAdmin):
    resource_class = Contract1000Resource
    contract_category = "1000"


@admin.register(ContractBachelorDiploma)
class ContractBachelorDiplomaAdmin(ContractCategoryAdmin):
    resource_class = ContractBachelorDiplomaResource
    contract_category = "bachelor"


@admin.register(ContractSecondary)
class ContractSecondaryAdmin(ContractCategoryAdmin):
    resource_class = ContractSecondaryResource
    contract_category = "secondary"


@admin.register(Wage)
class WageAdmin(ImportExportModelAdmin):
    resource_class = WageResource
    list_display = ("code", "name", "days", "daily_amount", "bonuses", "total_amount")
    search_fields = ("code", "name")
    ordering = ("name",)
