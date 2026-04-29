import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees_system.settings')
django.setup()

from employees.models import Employee

file_path = r"C:\Users\LENOVO\Desktop\employees_system\employees.xlsx"

df = pd.read_excel(file_path)

for index, row in df.iterrows():
    Employee.objects.create(
        emp_id=row['التسلسل'],  # استخدمناه كرقم وظيفي
        name=row['اسم الموظف'],
        job_title=row['عنوان وظيفي'],
        grade=row['د وظيفية'],
        stage=row['المرحلة'],

        base_salary=row['الراتب'],

        marital_status=row['الزوجية'],
        children=row['الاطفال'],

        position=row['المنصب'],
        certificate=row['الشهادة'],

        location=row['موقع جغرافي'],

        # دمج المخصصات
        risk_type=str(row['مهنية']) + " / " + str(row['الهندسية']) + " / " + str(row['الخطورة']),

        bonuses=row['مكافئات'],
        overtime=row['ساعات اضافية'],

        total=row['المجموع'],

        retirement=row['التقاعد'],
        tax=row['الضريبة'],
        deductions=row['الاستقطاعات'],
        social_security=row['صندوق الضمان الاجتماعي'],

        net_salary=row['الصافي']
    )

print("تم استيراد البيانات بنجاح ✅")