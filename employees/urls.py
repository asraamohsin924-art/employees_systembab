from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('salary/', views.salary_lookup, name='salary_lookup'),
    path('contracts/', views.contract_categories, name='contract_categories'),
    path('wages/', views.wage_lookup, name='wage_lookup'),
    path('contracts/<str:category>/', views.contract_lookup, name='contract_lookup'),
    path('logout/', views.logout_view, name='logout'),
    path('pdf/<str:emp_id>/', views.generate_pdf, name='generate_pdf'),
    path('info-pdf/<str:emp_id>/', views.employee_info_pdf, name='employee_info_pdf'),
    path('info/<str:emp_id>/', views.employee_info, name='employee_info'),
]
