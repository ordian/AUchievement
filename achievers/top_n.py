#coding=utf-8

import operator
import os
import sys
from achievers import top_n_achieveList


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def top_n_achiever(course_code, top_num):
    """
    Топ top_num студентов по предмету courseCode
    @param course_code: предмет по которому строится топ
    @param top_num: нужное число студентов в топе
    """
    achieve_code = "{0}_{1}_{2}".format("TOP", top_num, course_code)
    achieve_name = top_n_achieveList.achieve_list[course_code]
    achieve = Achievement.objects.get_or_create(code=achieve_code, description=achieve_name)[0]
    course_id = Course.objects.get(course_code=course_code).pk

    score_sum = {}
    student_dict = {}
    for student in Student.objects.all():
        student_dict[student.pk] = student
        score_sum[student.pk] = 0
    for mark in Mark.objects.filter(courseID=course_id):
        score_sum[mark.studentID.pk] += mark.result

    sorted_sum = sorted(score_sum.iteritems(), key=operator.itemgetter(1), reverse=True)

    for student_id, value in sorted_sum[:top_num]:
        AchievedAchievement.objects.get_or_create(achievementID=achieve, studentID=student_dict[student_id])