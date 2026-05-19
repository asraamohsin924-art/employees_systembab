from django.shortcuts import render
from .models import Employee
from weasyprint import HTML
from django.http import HttpResponse
from django.contrib.auth import logout

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


def generate_pdf(request, emp_id):
    employee = Employee.objects.filter(emp_id=emp_id).first()

    html = render(request, 'salary_pdf.html', {
        'employee': employee
    }).content.decode('utf-8')

    pdf = HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="salary.pdf"'

    return response