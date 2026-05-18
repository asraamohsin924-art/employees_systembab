from import_export import resources
from .models import Employee


class EmployeeResource(resources.ModelResource):

    class Meta:
        model = Employee

    def before_import_row(self, row, **kwargs):

        numeric_fields = [
            'الراتب',
            'الاطفال',
            'الاضافات',
            'مكافئات',
            'ساعات اضافية',
            'المجموع',
            'التقاعد',
            'الضريبة',
            'الاستقطاعات',
            'صندوق الضمان الاجتماعي',
            'الصافي',
        ]

        for field in numeric_fields:
            if row.get(field) in ['', ' ', None]:
                row[field] = 0