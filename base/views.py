from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.

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
    return render(request, 'login.html', context)


def do_login(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = request.POST.get("email")

        if user is not None:
            return HttpResponseRedirect(f'/parent/{"Tatenda Chirume"}')
        else:
            return HttpResponseRedirect("/")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def teacher_home(request, teacher_name):
    context = {
        'teacher_name': teacher_name
    }
    return render(request, 'teacher/home.html', context)


def student_home(request, student_name):
    context = {
        'student_name': student_name
    }
    return render(request, 'student/home.html', context)


def registrar_home(request):
    return render(request, 'registrar/registrar_layout.html')


def accountant_home(request):
    return render(request, 'accountant/home.html')


def parent_home(request, parent_name):
    context = {'parent_name': parent_name}
    return render(request, 'parent/home.html', context)


def parent_payments(request):
    payments = [
        {'date': '2021-02-01', 'tender': 'USD', 'type': 'Invoice', 'amount': 100, 'description': 'Academic Fees'},
        {'date': '2021-03-02', 'tender': 'USD', 'type': 'Invoice', 'amount': 100,
         'description': 'Students Medical Aid'},
        {'date': '2021-04-02', 'tender': 'ZWL', 'type': 'Invoice', 'amount': 100, 'description': 'Sports Levy'},
        {'date': '2021-05-09', 'tender': 'USD', 'type': 'Invoice', 'amount': 100, 'description': 'Lab Fees'},
        {'date': '2021-06-31', 'tender': 'ZWL', 'type': 'Invoice', 'amount': 100, 'description': 'Field Fees'},
        {'date': '2021-07-11', 'tender': 'USD', 'type': 'Invoice', 'amount': 100, 'description': 'Club Levy'},
        {'date': '2021-08-21', 'tender': 'USD', 'type': 'Invoice', 'amount': 100,
         'description': 'Infrastructure Develop levy'},
    ]
    context = {
        'payments': payments
    }
    return render(request, 'parent/payments.html', context)


def parent_invoices_receipts(request):
    render(request, 'parent/invoices-receipts.html')


def parent_ca(request):
    return render(request, 'parent/continuous-assessment.html')


def parent_report(request, child_name):
    results = [
        {
            'child_name': 'Brendon Chirume',
            'form': 'Form 1',
            'term': 'Term 1',
            'parent_comment': 'Brendon has been working hard and he has improved his marks',
            'marks': [
                {'subject': 'English Language', 'mark': 74, 'remark': 'well done'},
                {'subject': 'Shona / Ndebele', 'mark': 48, 'remark': 'she has to put more effort to improve'},
                {'subject': 'Geography', 'mark': 60, 'remark': 'she has worked well'},
                {'subject': 'FRS', 'mark': '', 'remark': ''},
                {'subject': 'Mathematics', 'mark': 83, 'remark': 'Excellent work keep it up'},
                {'subject': 'Accounting', 'mark': 25, 'remark': 'work hard to improve'},
                {'subject': 'Combined Science', 'mark': 76, 'remark': 'she has worked well'},
                {'subject': 'Computer Science', 'mark': '', 'remark': ''},
                {'subject': 'Art', 'mark': 63, 'remark': 'A satisfactory mark'},
                {'subject': 'Agriculture', 'mark': 76, 'remark': 'A good mark'},
                {'subject': 'Heritage Studies', 'mark': '', '': ''},
                {'subject': 'Physical education', 'mark': 75, 'remark': 'A very good mark'},
            ]
        }, {
            'child_name': 'Tatenda Chirume',
            'form': 'Form 1',
            'term': 'Term 1',
            'parent_comment': 'Brendon has been working hard and he has improved his marks',
            'marks': [
                {'subject': 'English Language', 'mark': 74, 'remark': 'well done'},
                {'subject': 'Shona / Ndebele', 'mark': 48, 'remark': 'she has to put more effort to improve'},
                {'subject': 'Geography', 'mark': 60, 'remark': 'she has worked well'},
                {'subject': 'FRS', 'mark': '', 'remark': ''},
                {'subject': 'Mathematics', 'mark': 83, 'remark': 'Excellent work keep it up'},
                {'subject': 'Accounting', 'mark': 25, 'remark': 'work hard to improve'},
                {'subject': 'Combined Science', 'mark': 76, 'remark': 'she has worked well'},
                {'subject': 'Computer Science', 'mark': '', 'remark': ''},
                {'subject': 'Art', 'mark': 63, 'remark': 'A satisfactory mark'},
                {'subject': 'Agriculture', 'mark': 76, 'remark': 'A good mark'},
                {'subject': 'Heritage Studies', 'mark': '', '': ''},
                {'subject': 'Physical education', 'mark': 75, 'remark': 'A very good mark'},
            ]
        }
    ]
    context = {'child_name': child_name, 'results': results}
    return render(request, 'parent/reports.html', context)


def principal_home(request, principal_name):
    context = {'principal_name': principal_name}
    return render(request, 'principal/home.html', context=context)


def principal_teachers(request):
    context = {
        'teachers': [
            {
                'id': 1,
                'first_name': 'Brendon',
                'last_name': 'Chirume',
                'gender': 'male',
                'dob': '11/02/98',
                'class': '1 Diamond',
                # 'subjects': ['maths', 'english', 'chemistry', 'biology', 'physics'],
                'subject': 'Physics',
                'phone': '0776445843',
                'email': 'Brendon.Chirume@example.com'
            }, {
                'id': 2,
                'first_name': 'Pamela',
                'last_name': 'Ncube',
                'gender': 'female',
                'dob': '11/02/98',
                'class': '7 Silver',
                # 'subjects': ['maths', 'english', 'chemistry', 'biology', 'physics'],
                'subject': 'Mathematics',
                'phone': '0776445843',
                'email': 'Pamela.Ncube@example.com'
            }, {
                'id': 3,
                'first_name': 'Jameson',
                'last_name': 'Nyamupaguma',
                'gender': 'male',
                'dob': '11/02/98',
                'class': '5 Gold',
                # 'subjects': ['maths', 'english', 'chemistry', 'biology', 'physics'],
                'subject': 'English',
                'phone': '0776445843',
                'email': 'Jameson.Nyamupaguma@example.com'
            },
        ]
    }
    return render(request, 'principal/teachers.html', context=context)


def principal_students(request):
    return render(request, 'principal/students.html')


def principal_reports(request):
    return render(request, 'principal/reports.html')


def principal_subjects(request):
    context = {
        'subjects': [
            {
                'code': 'SCI1200',
                'name': 'Mathematics',
            }, {
                'code': 'SCI1201',
                'name': 'English'
            }, {
                'code': 'SCS1202',
                'name': 'Shona'
            }, {
                'code': 'SAS1203',
                'name': 'Chemistry'
            }, {
                'code': 'SCI1204',
                'name': 'Religious Studies'
            },
        ]
    }
    return render(request, 'principal/subjects.html', context=context)
