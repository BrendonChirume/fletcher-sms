from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Teacher(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


def __str__(self):
    return self.username


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.EmailField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
