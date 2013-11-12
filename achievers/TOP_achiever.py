#coding=utf-8

import operator
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


course_to_top = {}
course_to_top["GT"]  = "графоман"
course_to_top["CO"]  = "комбинатор"
course_to_top["AS"]  = "и ужасный"
course_to_top["AL1"] = "алгоритмист"
course_to_top["AL2"] = "алгоритмист"
course_to_top["ML1"] = "и логичный"
course_to_top["ML2"] = "и логичный"
course_to_top["UX"]  = "питонист-башолюб"


def TOP_achieve(courseCode, achieve_descr, top_num):
    """
    Топ top_num студентов по предмету courseCode
    @param courseCode: предмет по которому строится топ
    @param achieve_name: имя ачивки
    @param top_num: нужное число студентов в топе
    """
    achieve = Achievement.objects.get_or_create(achievement=courseCode, description=achieve_descr, defaults={})[0]
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
# TOP_achieve('CO', u"Великие комбинаторы", 10)
