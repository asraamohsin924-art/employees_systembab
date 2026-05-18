from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Employee


class EmployeeResource(resources.ModelResource):

    emp_id = fields.Field(attribute='emp_id', column_name='التسلسل')
    name = fields.Field(attribute='name', column_name='اسم الموظف')
    job_title = fields.Field(attribute='job_title', column_name='عنوان وظيفي')
    grade = fields.Field(attribute='grade', column_name='د وظيفية')
    stage = fields.Field(attribute='stage', column_name='المرحلة')
    base_salary = fields.Field(attribute='base_salary', column_name='الراتب')
    marital_status = fields.Field(attribute='marital_status', column_name='الزوجية')
    children = fields.Field(attribute='children', column_name='الاطفال')
    position = fields.Field(attribute='position', column_name='المنصب')
    certificate = fields.Field(attribute='certificate', column_name='الشهادة')
    location = fields.Field(attribute='location', column_name='موقع جغرافي')
    professional = fields.Field(attribute='professional', column_name='مهنية')
    engineering = fields.Field(attribute='engineering', column_name='الهندسية')
    risk_type = fields.Field(attribute='risk_type', column_name='الخطورة')
    allowances = fields.Field(attribute='allowances', column_name='الاضافات')
    bonuses = fields.Field(attribute='bonuses', column_name='مكافئات')
    overtime = fields.Field(attribute='overtime', column_name='ساعات اضافية')
    total = fields.Field(attribute='total', column_name='المجموع')
    retirement = fields.Field(attribute='retirement', column_name='التقاعد')
    tax = fields.Field(attribute='tax', column_name='الضريبة')
    deductions = fields.Field(attribute='deductions', column_name='الاستقطاعات')
    social_security = fields.Field(attribute='social_security', column_name='صندوق الضمان الاجتماعي')
    final_total = fields.Field(attribute='final_total', column_name='المجموع.1')
    net_salary = fields.Field(attribute='net_salary', column_name='الصافي')

    class Meta:
        model = Employee


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource