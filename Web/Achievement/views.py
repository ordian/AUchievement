from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from Achievement.models import *

def new_student(request):
  student = Student()
  student.name = "Semyon"
  student.surname = "Atamas"



def dashboard(request):
  return redirect('statistics/')

def people(request):
  return render(request, 'Achievement/people.html')

def statistics(request):
  return render(request, 'Achievement/statistics.html')

def achievements(request):
  return render(request, 'Achievement/achievements.html')
