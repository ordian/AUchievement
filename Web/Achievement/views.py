import datetime
from django.shortcuts import render
from django.shortcuts import redirect

from models import Student, Course, Mark


def addStudents(nameList):
    for t in nameList:
        student = Student(first_name=t['name'], last_name=t['surname'])
        student.save()


def addCourses(courseList):
    for i in courseList:
        course = Course(course_name=i['subject'], course_code = i['code'])
        course.save()


def addMark(student, course, hw, task, date, score):
    m = Mark(studentID=student, courseID=course, hwNo=hw, taskNo=task, date=date, result=score)
    m.save()


def dashboard(request):
    return redirect('statistics/')


def people(request):
    people = Student.objects.all()
    return render(request, 'Achievement/people.html', {'people': people})


def statistics(request):
    return render(request, 'Achievement/statistics.html')


def achievements(request):
    return render(request, 'Achievement/achievements.html')
