from django.shortcuts import render
from .models import Employee
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

import pandas as pd
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
def to_int(value):
    if value is None:
        return 0
    value = str(value).strip()
    if value == '' or value.lower() == 'nan':
        return 0
    return int(float(value))
@staff_member_required

def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('salary_lookup')
        else:
            error = "بيانات الدخول غير صحيحة"

    return render(request, "login.html", {"error": error})
@login_required
def salary_lookup(request):
    employee = None
    error = None

    if request.method == "POST":
        emp_id = request.POST.get("emp_id")

        if emp_id:
            emp_id = emp_id.strip()

            employee = Employee.objects.filter(
    emp_id=str(emp_id)
).first()

            if not employee:
                error = "لا يوجد موظف بهذا الرقم"
        else:
            error = "الرجاء إدخال الرقم الوظيفي"

    return render(request, "salary.html", {
        "employee": employee,
        "error": error
    })

# 👇 هنا تضيفها (تحتها مباشرة)
def logout_view(request):
    logout(request)
    return redirect('login')
def generate_pdf(request, emp_id):
    employee = Employee.objects.filter(emp_id=emp_id).first()

    html = render(request, 'salary_pdf.html', {
        'employee': employee
    }).content.decode('utf-8')

    pdf = HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="salary.pdf"'

    return response