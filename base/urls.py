from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-user/', views.add_student, name='add-student'),
    path('subjects/', views.subjects, name='subjects'),
    path('enroll/', views.enroll, name='enroll'),
    path('reports/', views.reports, name='reports'),
    path('student-report/<str:student_id>/', views.student_report, name='studentReportCard'),
    path('teachers/', views.teachers, name='teachers'),
    path('parents/', views.teachers, name='parents'),
    path('students/', views.students, name='students'),
    path('login/', views.login, name='login'),
]

handler404 = 'base.views.handler404'
