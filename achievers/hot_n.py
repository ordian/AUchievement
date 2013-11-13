# coding=utf-8
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def hot_n_achiever(course_code, limit_list):
    """
    Проставляет всем студентам ачивку "решил N задач по указанному предмету"
    @param limit_list: сколько баллов надо набрать, чтобы получить ачивку (передается общим списком)
    @param course_code: код курса (GT or AL1 и так далее)
    """
    achievements = {}

    for limit in limit_list:
        achieve_code = "{0}_{1}_{2}".format("HOT", limit, course_code)
        achievements[limit] = Achievement.objects.get_or_create(code=achieve_code)[0]

    course_id = Course.objects.get(course_code=course_code).pk

    score_sum = {}
    student_dict = {}
    for student in Student.objects.all():
        student_dict[student.pk] = student
        score_sum[student.pk] = 0

    for mark in Mark.objects.filter(courseID=course_id):
        score_sum[mark.studentID.pk] += mark.result

    for student_id in score_sum.keys():
        for limit in limit_list:
            if score_sum[student_id] >= limit:
                AchievedAchievement.objects.get_or_create(achievementID=(achievements[limit]), studentID=student_dict[student_id])