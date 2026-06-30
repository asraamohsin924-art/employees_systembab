from import_export import resources, fields
from .models import Employee, EmployeeInfo


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


class EmployeeInfoResource(resources.ModelResource):

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