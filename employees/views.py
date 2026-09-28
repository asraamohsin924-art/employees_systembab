from django.shortcuts import render, redirect
from .models import Employee, EmployeeInfo, Contract, Wage
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
from django.contrib.auth import logout


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "12345678":
            request.session["employee_access"] = True
            return redirect("home")
        error = "اسم المستخدم أو كلمة المرور غير صحيحة"
    return render(request, "login.html", {"error": error})


def home(request):
    if not request.session.get("employee_access"):
        return redirect("login")
    return render(request, "home.html")


def salary_lookup(request):
    if not request.session.get("employee_access"):
        return redirect("login")

    employee = None
    error = None
    if request.method == "GET" and request.GET.get("show") == "salary":
        emp_id = request.GET.get("emp_id")
        if emp_id:
            employee = Employee.objects.filter(emp_id=str(emp_id).strip()).first()
    elif request.method == "POST":
        emp_id = (request.POST.get("emp_id") or "").strip()
        if emp_id:
            employee = Employee.objects.filter(emp_id=emp_id).first()
            if not employee:
                error = "لا يوجد موظف بهذا الرقم"
        else:
            error = "الرجاء إدخال الكود"

    return render(request, "salary.html", {"employee": employee, "error": error})


def contract_categories(request):
    if not request.session.get("employee_access"):
        return redirect("login")
    return render(request, "contract_categories.html")


def contract_lookup(request, category):
    if not request.session.get("employee_access"):
        return redirect("login")
    valid = dict(Contract.CATEGORY_CHOICES)
    if category not in valid:
        return redirect("contract_categories")

    contract = None
    error = None
    if request.method == "POST":
        code = (request.POST.get("code") or "").strip()
        if code:
            contract = Contract.objects.filter(category=category, code__iexact=code).first()
            if not contract:
                error = "لا يوجد عقد بهذا الكود ضمن هذا القسم"
        else:
            error = "الرجاء إدخال الكود"

    return render(request, "contract_lookup.html", {
        "contract": contract,
        "error": error,
        "category": category,
        "category_name": valid[category],
    })


def wage_lookup(request):
    if not request.session.get("employee_access"):
        return redirect("login")

    wage = None
    error = None
    if request.method == "POST":
        code = (request.POST.get("code") or "").strip()
        if code:
            wage = Wage.objects.filter(code__iexact=code).first()
            if not wage:
                error = "لا توجد بيانات أجور بهذا الكود"
        else:
            error = "الرجاء إدخال الكود"

    return render(request, "wage_lookup.html", {"wage": wage, "error": error})


def logout_view(request):
    logout(request)
    return redirect("login")


def generate_pdf(request, emp_id):
    if not request.session.get("employee_access"):
        return redirect("login")
    employee = Employee.objects.filter(emp_id=emp_id).first()
    template = get_template("salary_pdf.html")
    html = template.render({"employee": employee})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="salary.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("حدث خطأ أثناء إنشاء ملف PDF")
    return response


def employee_info_pdf(request, emp_id):
    if not request.session.get("employee_access"):
        return redirect("login")
    info = EmployeeInfo.objects.filter(emp_id=emp_id).first()
    return render(request, "employee_info_pdf.html", {"info": info})


def employee_info(request, emp_id):
    if not request.session.get("employee_access"):
        return redirect("login")
    info = EmployeeInfo.objects.filter(emp_id=emp_id).first()
    return render(request, "employee_info.html", {"info": info})
