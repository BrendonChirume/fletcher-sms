from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.subjects, name='subjects'),
    path('login/', views.login, name='login'),
]

handler404 = 'base.views.handler404'
