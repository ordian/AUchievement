# coding=utf-8

import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum, Max
from django.db import connection

from models import Student, Course, Mark, AchievedAchievement, Achievement


def addStudents(nameList):
    for t in nameList:
        student = Student(first_name=t['name'], last_name=t['surname'])
        student.save()


def addCourses(courseList):
    for i in courseList:
        course = Course(course_name=i['subject'], course_code=i['code'])
        course.save()


def addMark(student, course, hw, task, date, score):
    m = Mark(studentID=student, courseID=course, hwNo=hw, taskNo=task, date=date, result=score)
    m.save()


def dashboard(request):
    return redirect('people/')


def people(request):
    people = Student.objects.all()
    return render(request, 'Achievement/people.html', {'people': people})


def statistics(request, id):
    student = Student.objects.get(id=id)
    marks = Mark.objects.filter(studentID__exact=student.id)

    course_mark = dict()

    courses_list = []
    for mark in marks:
        course_name = mark.courseID.course_name
        if course_name not in course_mark:
            course_mark[course_name] = dict()
            courses_list.append(course_name)

        if mark.hwNo not in course_mark[course_name]:
            course_mark[course_name][mark.hwNo] = 0

        course_mark[course_name][mark.hwNo] += mark.result

    courses_list.sort()
    homework_completion = dict()
    for course in courses_list:
        homework_completion[course] = {
            'homeworks': list(sorted(course_mark[course].keys())),
            'completion': course_mark[course]
        }

    courses = Course.objects.all();
    course_overall = dict()
    for course in courses:
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT SUM(course_marks.task_max_result)
        FROM
        (SELECT taskNo, MAX(result) as task_max_result
        FROM achievement_mark 
        WHERE courseID_id=%s 
        GROUP BY taskNo) course_marks''',
            [course.id])
        total = cursor.fetchone()[0]

        student_marks = Mark.objects.filter(studentID__exact=student.id)
        course_marks = student_marks.filter(courseID__exact=course.id)
        current = course_marks.aggregate(Sum('result')).values()[0]
        if current is None:
            percent = 0
        else:
            percent_f = round(current / total * 100)
            percent = min(int(percent_f), 100)

        course_overall[course.course_name] = percent

    data = {
        'courses': courses_list,
        'activities': homework_completion,
        'overall': course_overall,
        'name': student.first_name + ' ' + student.last_name
    }

    return render(request, 'Achievement/statistics.html', data)


def achievements(request, id):
    student = Student.objects.get(id=id)
    achieves = AchievedAchievement.objects.filter(studentID__exact=student.id)
    achievements = [achieve.achievementID for achieve in achieves]

    badges = []
    for ach in achievements:
        badge = dict()
        badge['image'] = ach.image

        code = ach.code
        code = code.replace('FULL_HW', 'FULLHW')

        a_type, param, course_code = code.split('_')

        if a_type == 'FULLHW':
            badge['name'] = u'Полное ДЗ %s' % (param,)
        elif a_type == 'HOT':
            badge['name'] = u'Решил %s задач' % (param,)
        elif a_type == 'TOP':
            badge['name'] = u'Топ %s' % (param,)

        course_name = Course.objects.get(course_code__exact=course_code).course_name
        badge['description'] = course_name

        badges.append(badge)

    data = {
        'achievements': badges,
        'name': student.first_name + ' ' + student.last_name
    }

    return render(request, 'Achievement/achievements.html', data)
