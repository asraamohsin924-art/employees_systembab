from import_export import resources, fields
from django.conf import settings
from django.db import transaction, connections
from pathlib import Path
from datetime import datetime
import shutil

from .models import Employee, EmployeeInfo, Contract, Contract1000, ContractBachelorDiploma, ContractSecondary, Wage




class ReplaceAllResourceMixin:
    """Safely replace the dataset during a confirmed admin import.

    - Preview/dry-run never changes the database.
    - Excel headers are normalized by trimming surrounding whitespace.
    - On confirmed import, a database backup is created first.
    - Only this resource's dataset is replaced.
    - Any import error rolls the transaction back.
    """

    def get_replace_queryset(self):
        return self._meta.model.objects.all()

    def _normalize_headers(self, dataset):
        if not getattr(dataset, "headers", None):
            return
        # Excel files sometimes contain headers such as "الكود " with a
        # trailing space. Normalize the header text before import-export
        # validates import_id_fields.
        dataset.headers = [
            h.strip() if isinstance(h, str) else h
            for h in dataset.headers
        ]

    def _backup_database(self):
        db_name = connections["default"].settings_dict.get("NAME")
        if not db_name or db_name == ":memory:":
            return None

        db_path = Path(str(db_name))
        if not db_path.exists():
            return None

        if str(db_path).startswith("/var/data/"):
            backup_dir = db_path.parent / "import_backups"
        else:
            backup_dir = Path(settings.BASE_DIR) / "import_backups"

        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"db_before_import_{stamp}.sqlite3"
        shutil.copy2(db_path, backup_path)

        backups = sorted(
            backup_dir.glob("db_before_import_*.sqlite3"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        for old_backup in backups[5:]:
            try:
                old_backup.unlink()
            except OSError:
                pass
        return backup_path

    def import_data(self, dataset, dry_run=False, *args, **kwargs):
        # Normalize headers before django-import-export checks import_id_fields.
        self._normalize_headers(dataset)

        if dry_run:
            return super().import_data(dataset, dry_run=True, *args, **kwargs)

        self._backup_database()
        with transaction.atomic():
            self.get_replace_queryset().delete()
            result = super().import_data(dataset, dry_run=False, *args, **kwargs)
            if result.has_errors() or result.has_validation_errors():
                transaction.set_rollback(True)
            return result


class EmployeeResource(ReplaceAllResourceMixin, resources.ModelResource):

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
    professional = fields.Field(attribute='professional', column_name='مهنية + خطورة')
    engineering = fields.Field(attribute='engineering', column_name='الهندسية')
    
    allowances = fields.Field(attribute='allowances', column_name='الاضافات')
    bonuses = fields.Field(attribute='bonuses', column_name='مكافئات')
    overtime = fields.Field(attribute='overtime', column_name='ساعات اضافية')
    total = fields.Field(attribute='total', column_name='مجموع الاستحقاق')
    retirement = fields.Field(attribute='retirement', column_name='التقاعد')
    tax = fields.Field(attribute='tax', column_name='الضريبة')
    deductions = fields.Field(attribute='deductions', column_name='الاستقطاعات')
    social_security = fields.Field(attribute='social_security', column_name='صندوق الضمان الاجتماعي')
    final_total = fields.Field(attribute='final_total', column_name='مجموع الاستقطاع')
    net_salary = fields.Field(attribute='net_salary', column_name='الصافي')

    class Meta:
        model = Employee


class EmployeeInfoResource(ReplaceAllResourceMixin, resources.ModelResource):

    emp_id = fields.Field(attribute='emp_id', column_name='التسلسل')
    full_name = fields.Field(attribute='full_name', column_name='الاسم الرباعي واللقب')
    birth_date = fields.Field(attribute='birth_date', column_name='المواليد')
    mother_name = fields.Field(attribute='mother_name', column_name='اسم الام الثلاثي')
    gender = fields.Field(attribute='gender', column_name='الجنس')
    employment_type = fields.Field(attribute='employment_type', column_name='نوع التعيين')
    marital_status = fields.Field(attribute='marital_status', column_name='الحالة الزوجية')
    appointment_order = fields.Field(attribute='appointment_order', column_name='رقم امر التعيين')
    appointment_order_date = fields.Field(attribute='appointment_order_date', column_name='تاريخ امر التعيين')
    start_date = fields.Field(attribute='start_date', column_name='تاريخ المباشرة')
    basic_salary = fields.Field(attribute='basic_salary', column_name='الراتب الاسمي')
    job_title = fields.Field(attribute='job_title', column_name='العنوان الوظيفي')
    education = fields.Field(attribute='education', column_name='التحصيل الدراسي')
    specialization = fields.Field(attribute='specialization', column_name='الاختصاص')
    grade = fields.Field(attribute='grade', column_name='الدرجة الوظيفية')
    stage = fields.Field(attribute='stage', column_name='المرحلة')
    last_bonus = fields.Field(attribute='last_bonus', column_name='تاريخ اخر علاوة')
    last_promotion = fields.Field(attribute='last_promotion', column_name='تاريخ اخر ترفيع')
    department = fields.Field(attribute='department', column_name='الشعبة')
    notes = fields.Field(attribute='notes', column_name='الملاحظات')
    graduation_year = fields.Field(attribute='graduation_year', column_name='سنة التخرج')
    service_duration = fields.Field(attribute='service_duration', column_name='مدة الخدمة')

    class Meta:
        model = EmployeeInfo
        import_id_fields = ('emp_id',)

class ContractResource(resources.ModelResource):
    class Meta:
        model = Contract
        import_id_fields = ('category', 'code')


class Contract1000Resource(ReplaceAllResourceMixin, ContractResource):
    class Meta:
        model = Contract1000
        import_id_fields = ('code',)

    def get_replace_queryset(self):
        return self._meta.model.objects.filter(category='1000')

    def before_import_row(self, row, **kwargs):
        row['category'] = '1000'


class ContractBachelorDiplomaResource(ReplaceAllResourceMixin, ContractResource):
    class Meta:
        model = ContractBachelorDiploma
        import_id_fields = ('code',)

    def get_replace_queryset(self):
        return self._meta.model.objects.filter(category='bachelor')

    def before_import_row(self, row, **kwargs):
        row['category'] = 'bachelor'


class ContractSecondaryResource(ReplaceAllResourceMixin, ContractResource):
    class Meta:
        model = ContractSecondary
        import_id_fields = ('code',)

    def get_replace_queryset(self):
        return self._meta.model.objects.filter(category='secondary')

    def before_import_row(self, row, **kwargs):
        row['category'] = 'secondary'


class WageResource(ReplaceAllResourceMixin, resources.ModelResource):
    code = fields.Field(attribute="code", column_name="الكود")
    name = fields.Field(attribute="name", column_name="الاسم")
    days = fields.Field(attribute="days", column_name="عدد الايام")
    daily_amount = fields.Field(attribute="daily_amount", column_name="المبلغ اليومي")
    bonuses = fields.Field(attribute="bonuses", column_name="المكافئات")
    total_amount = fields.Field(attribute="total_amount", column_name="المبلغ الكلي")

    class Meta:
        model = Wage
        import_id_fields = ("code",)
