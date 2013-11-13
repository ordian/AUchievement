from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)


class Mark(models.Model):
    studentID = models.ForeignKey(Student)
    courseID = models.ForeignKey(Course)
    hwNo = models.IntegerField()
    taskNo = models.CharField(max_length=20)
    date = models.DateTimeField()
    result = models.FloatField()


class Achievement(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=1000, blank=True)


class AchievedAchievement(models.Model):
    achievementID = models.ForeignKey(Achievement)
    studentID = models.ForeignKey(Student)