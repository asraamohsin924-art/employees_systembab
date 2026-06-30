
from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)  # الرقم الوظيفي
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    stage = models.CharField(max_length=50)

    base_salary = models.IntegerField()

    marital_status = models.CharField(max_length=50)
    children = models.IntegerField()

    position = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)

    location = models.CharField(max_length=100)
    risk_type = models.CharField(max_length=100, blank=True, default="")
    
    professional = models.IntegerField(default=0)   # مهنية
    engineering = models.IntegerField(default=0)    # الهندسية
    allowances = models.IntegerField(default=0)     # الاضافات
    final_total = models.IntegerField(default=0)    # المجموع الثاني
    bonuses = models.IntegerField()
    overtime = models.IntegerField()

    total = models.IntegerField()

    retirement = models.IntegerField()
    tax = models.IntegerField()
    deductions = models.IntegerField()
    social_security = models.IntegerField()

    net_salary = models.IntegerField()

    def __str__(self):
        return self.name
        
        
class EmployeeInfo(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)

    full_name = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    employment_type = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)

    appointment_order = models.CharField(max_length=100, blank=True, null=True)
    appointment_order_date = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)

    basic_salary = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    grade = models.CharField(max_length=50, blank=True, null=True)
    stage = models.CharField(max_length=50, blank=True, null=True)

    last_bonus = models.CharField(max_length=50, blank=True, null=True)
    last_promotion = models.CharField(max_length=50, blank=True, null=True)

    department = models.CharField(max_length=100, blank=True, null=True)
    #result = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    graduation_year = models.CharField(max_length=20, blank=True, null=True)
    service_duration = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name or self.emp_id
# Create your models here.
