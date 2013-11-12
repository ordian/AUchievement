# coding=utf-8
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from django.db.models import Max
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def full_hw_achiever(course_code):
    """
    Проставляет ачивку студентам, которые сделали всю домашку
    @param course_code: код курса
    """
    course_id = Course.objects.get(course_code=course_code).pk

    lastHW = Mark.objects.filter(courseID=course_id).aggregate(Max('hwNo'))
    hw_max = lastHW['hwNo__max']

    for student in Student.objects.all():
        marks = Mark.objects.filter(courseID=course_id, studentID=student)
        for hw_number in range(1, hw_max + 1):
            achieve_code = "{0}_{1}_{2}".format("FULL_HW", hw_number, course_code)
            achieve = Achievement.objects.get_or_create(code=achieve_code)[0]
            hw_marks = marks.filter(hwNo=hw_number)
            hw_done = True
            if len(hw_marks) != 0:
                if any(mark.result < 1 for mark in hw_marks):
                    hw_done = False
            else:
                hw_done = False

            if hw_done:
                AchievedAchievement.objects.get_or_create(achievementID=achieve, studentID=student)