import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement

def whole_hw_achiever(courseCode, achieve_name, hwN):
    achieve = Achievement.objects.get_or_create(achievement = achieve_name, defaults ={})[0]
    course = Course.objects.get(course_code=courseCode)

    for student in Student.objects.all():
        marks=Mark.objects.filter(courseID = course, studentID=student, hwNo = hwN)
        allHW = True
        if (marks.__len__() != 0):
            for mark in marks:
                if mark.result==0:
                    allHW = False
        else:
            allHW = False
        if allHW:
            AchievedAchievement.objects.get_or_create( achievementID = achieve, studentID = student,  defaults={})


def course_total_achiever( limit , courseCode, achieve_name):
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

hwN=1
whole_hw_achiever('AS', 'allHot', hwN)