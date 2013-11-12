#coding=utf-8

import operator
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def TOP_achieve(courseCode, achieve_name, top_num):
    """
    @param courseCode: предмет по которому строится топ
    @param achieve_name: имя ачивки
    @param top_num: нужное число студентов в топе
    """
    achieve = Achievement.objects.get_or_create(achievement=courseCode, description=achieve_name, defaults={})[0]
    course = Course.objects.get(course_code=courseCode)
    summ = {}
    for student in Student.objects.all():
        summ[student.pk] = 0
    for mark in Mark.objects.filter(courseID=course.pk):
        summ[mark.studentID.pk] = summ[mark.studentID.pk] + mark.result
    
    sorted_summ = sorted(summ.iteritems(), key=operator.itemgetter(1), reverse=True)

    for id, value in sorted_summ[:top_num]:
            AchievedAchievement.objects.get_or_create(achievementID = achieve , studentID = Student.objects.get(pk = id), defaults={})

# example
TOP_achieve('CO', u"Великие комбинаторы", 10)
