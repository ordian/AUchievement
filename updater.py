# coding=utf-8
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
import logging
from timer import timer
from Web.Achievement.views import addMark
from Web.Achievement.models import Student, Course, Mark
from django.core.exceptions import ObjectDoesNotExist


@timer
def update(studentList):
    studentList = list(studentList)
    total = len(studentList)

    students_db = {}
    for s in Student.objects.all():
        students_db[(s.first_name, s.last_name)] = s

    courses_db = {}
    for c in Course.objects.all():
        courses_db[c.course_code] = c

    for num, current_student in enumerate(studentList):

        if num % 500 == 0:
            print "import {0}/{1}".format(num, total)

        try:
            student = students_db[(current_student.name, current_student.surname)]
        except:
            logging.error("student not found %s" % current_student)

        try:
            course = courses_db[current_student.subject]
        except:
            logging.error("course not found %s" % current_student)

        try:
            mark = Mark.objects.get(studentID=student.id, courseID=course.id,
                                    hwNo=current_student.hw, taskNo=current_student.task)

            # если оценка нашлась, смотрим, изменилась ли она
            new_mark = current_student.score
            old_mark = mark.result
            if old_mark != new_mark:
                # если изменилась, пишем новую
                mark.result = new_mark
                mark.date = current_student.date
                mark.save()
        except ObjectDoesNotExist: # если такой оценки не было, то записываем ее
            logging.info("writing new mark at student %s" % current_student)
            addMark(student, course, current_student.hw, current_student.task, current_student.date,
                    current_student.score)