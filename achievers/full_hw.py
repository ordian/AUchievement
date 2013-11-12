# coding=utf-8
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def full_hw_achiever(course_code):
    hw_number = 1 # TODO исправить!! Сделать так, чтобы домашка сама считалась
    achieve_code = "{0}_{1}_{2}".format("FULL_HW", hw_number, course_code)
    achieve = Achievement.objects.get_or_create(code=achieve_code)[0]
    course_id = Course.objects.get(course_code=course_code).pk

    for student in Student.objects.all():
        marks = Mark.objects.filter(courseID=course_id, studentID=student, hwNo=hw_number)
        hw_done = True
        if len(marks) != 0:
            if any(mark.result == 0 for mark in marks):
                hw_done = False
        else:
            hw_done = False

        if hw_done:
            AchievedAchievement.objects.get_or_create(achievementID=achieve, studentID=student)