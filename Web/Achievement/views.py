from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from Achievement.models import *

def new_student(request):
  student = Student()
  student.name = "Semyon"
  student.surname = "Atamas"



