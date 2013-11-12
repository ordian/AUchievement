import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def AS_achiever( limit , courseCode, achieve_name):
    achieve = Achievement.objects.get_or_create(achievement = achieve_name, defaults ={})[0]
    course = Course.objects.get(course_code=courseCode)
    summ={}
    for student in Student.objects.all():
        summ[ student.pk ]=0
    for mark in Mark.objects.filter(courseID = course.pk):
        summ[ mark.studentID.pk ] = summ[ mark.studentID.pk ]+mark.result
    for id in summ.keys():
        if summ[id] >= limit:
            AchievedAchievement.objects.get_or_create( achievementID = achieve , studentID = Student.objects.get(pk = id), defaults={})

limit=4
AS_achiever(4, 'AS', 'hot'+str(limit))