from django.contrib import admin
from django.urls import path, include
from base import views


urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('do-login', views.do_login, name="do_login"),

    path('teacher/<str:teacher_name>', views.teacher_home, name='teacher-main'),
    path('teacher/students/', views.principal_students, name='teacher-students'),
    path('teacher/subjects/', views.principal_subjects, name='teacher-subjects'),

    path('student/<str:student_name>/', views.student_home, name='student_home'),
    path('student/subjects/', views.principal_subjects, name='student_subjects'),
    path('student/report/', views.principal_reports, name='student_report'),

    path('principal/<str:principal_name>', views.principal_home, name='principal_home'),
    path('principal/teachers/', views.principal_teachers, name='principal_teachers'),
    path('principal/students/', views.principal_students, name='principal_students'),
    path('principal/subjects/', views.principal_subjects, name='principal_subjects'),
    path('principal/reports/', views.principal_reports, name='principal_reports'),

    path('registrar/<str:registrar_name>', views.registrar_home, name='registrar_profile'),

    path('parent/<str:parent_name>', views.parent_home, name='parent_home'),
    path('parent/exams/<str:child_name>/', views.parent_report, name='parent_child_marks'),
    path('parent/continuous-assessment/', views.parent_ca, name='parent_CA'),
    path('parent/payments-history/', views.parent_payments, name='parent_payments'),
    path('parent/invoices-and-receipts/', views.parent_invoices_receipts, name='parent_invoices_receipts'),

    path('accountant/accountant/', views.accountant_home, name='accountant_profile'),
]
