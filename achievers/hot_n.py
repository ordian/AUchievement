# coding=utf-8
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")
sys.path.append('Web')
from Web.Achievement.models import Mark, Course, Student, Achievement, AchievedAchievement


def hot_n_achiever(limit, course_code):
    """
    Проставляет всем студентам ачивку "решил N задач по указанному предмету"
    @param limit: сколько баллов надо набрать, чтобы получить ачивку
    @param course_code: код курса (GT or AL1 и так далее)
    """
    achieve_code = "{0}_{1}_{2}".format("HOT", limit, course_code)
    achievement = Achievement.objects.get_or_create(code=achieve_code)[0]
    course_id = Course.objects.get(course_code=course_code).pk

    score_sum = {}
    student_dict = {}
    for student in Student.objects.all():
        student_dict[student.pk] = student
        score_sum[student.pk] = 0

    for mark in Mark.objects.filter(courseID=course_id):
        score_sum[mark.studentID.pk] += mark.result

    for student_id in score_sum.keys():
        if score_sum[student_id] >= limit:
            AchievedAchievement.objects.get_or_create(achievementID=achievement, studentID=student_dict[student_id])