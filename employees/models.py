from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
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
    professional = models.IntegerField(default=0)
    engineering = models.IntegerField(default=0)
    allowances = models.IntegerField(default=0)
    final_total = models.IntegerField(default=0)
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
    notes = models.TextField(blank=True, null=True)
    graduation_year = models.CharField(max_length=20, blank=True, null=True)
    service_duration = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name or self.emp_id


class Contract(models.Model):
    CATEGORY_1000 = "1000"
    CATEGORY_BACHELOR = "bachelor"
    CATEGORY_SECONDARY = "secondary"
    CATEGORY_CHOICES = [
        (CATEGORY_1000, "عقود الألف درجة"),
        (CATEGORY_BACHELOR, "عقود البكالوريوس والدبلوم"),
        (CATEGORY_SECONDARY, "عقود إعدادية فما دون"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200, blank=True, default="")
    start_date = models.CharField(max_length=50, blank=True, default="")
    days = models.IntegerField(default=0)
    monthly_salary = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    absence_deduction = models.IntegerField(default=0)
    net_after_absence = models.IntegerField(default=0)
    pension_5 = models.IntegerField(default=0)
    net_salary = models.IntegerField(default=0)
    bank = models.CharField(max_length=100, blank=True, default="")
    workplace = models.CharField(max_length=200, blank=True, default="")
    phone = models.CharField(max_length=50, blank=True, default="")
    notes = models.TextField(blank=True, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["category", "code"], name="unique_contract_category_code")
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.code}"


class Wage(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    days = models.IntegerField(default=0)
    daily_amount = models.IntegerField(default=0)
    bonuses = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name = "الأجور"
        verbose_name_plural = "الأجور"

    def __str__(self):
        return f"{self.name} - {self.code}"

class Contract1000(Contract):
    class Meta:
        proxy = True
        verbose_name = "عقود الألف درجة"
        verbose_name_plural = "عقود الألف درجة"


class ContractBachelorDiploma(Contract):
    class Meta:
        proxy = True
        verbose_name = "عقود البكالوريوس والدبلوم"
        verbose_name_plural = "عقود البكالوريوس والدبلوم"


class ContractSecondary(Contract):
    class Meta:
        proxy = True
        verbose_name = "عقود إعدادية فما دون"
        verbose_name_plural = "عقود إعدادية فما دون"
