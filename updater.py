# coding=utf-8
import logging
import os
import sys
from timer import timer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from StudentInfo import StudentInfo
from Web.Achievement.views import addMark
from Web.Achievement.models import Student, Course, Mark
from django.core.exceptions import ObjectDoesNotExist


@timer
def update(studentList):
    studentList = list(studentList)
    total = len(studentList)
    for num, student_info in enumerate(studentList):
        assert isinstance(student_info, StudentInfo)
        
        if num % 500 == 0:
            print "{0}/{1}".format(num, total)

        try:
            student = Student.objects.get(first_name=student_info.name, last_name=student_info.surname)
        except:
            logging.error("student not found %s" % student_info)

        try:
            course = Course.objects.get(course_code=student_info.subject)
        except:
            logging.error("course not found %s" % student_info)

        try:
            mark = Mark.objects.get(studentID=student.id, courseID=course.id,
                                    hwNo=student_info.hw, taskNo=student_info.task)

            # если оценка нашлась, смотрим, изменилась ли она
            new_mark = student_info.score
            old_mark = mark.result
            if old_mark != new_mark:
                # если изменилась, пишем новую
                mark.result = new_mark
                mark.date = student_info.date
                mark.save()
        except ObjectDoesNotExist: # если такой оценки не было, то записываем ее
            logging.info("writing new mark at student %s" % student_info)
            addMark(student, course, student_info.hw, student_info.task, student_info.date, student_info.score)