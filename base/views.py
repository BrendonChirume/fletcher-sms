from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def subjects(request):
    return render(request, 'pages/subjects.html')


def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)


def login(request):
    return render(request, 'pages/login.html')
