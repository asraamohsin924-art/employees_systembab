
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
    risk_type = models.CharField(max_length=100)

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
# Create your models here.
