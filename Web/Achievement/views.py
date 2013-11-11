from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from Achievement.models import *

def new_achievement(request):
  achievment = Achievement()
  achievment.text = "Ho-ho Hero!"
  achievment.tasks_to_solve = 50
  achievment.save()

  return redirect('/achievement/view')

def view_achievements(request):
  achievements = Achievement.objects.all()
  return HttpResponse("You got %s achievements" % (len(achievements),))

