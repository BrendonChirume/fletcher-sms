from django.contrib.auth import authenticate
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def subjects(request):
    return render(request, 'pages/subjects.html')


def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)


def add_student(request):
    return render(request, 'pages/add-student.html')


def parents(request):
    return render(request, 'pages/parents.html')


def enroll(request):
    return render(request, 'pages/enroll.html')


def reports(request):
    return render(request, 'pages/reports.html')


def students(request):
    return render(request, 'pages/students.html')


def student_report(request, student_id):
    return render(request, 'pages/student_report_card.html', {'student_id': student_id})


def teachers(request):
    return render(request, 'pages/teachers.html')


def login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages

    context = {}
    return render(request, 'pages/login.html', context)
