from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Course(models.Model):
    course_name=models.CharField(max_length=30)

class Mark(models.Model):
    studentID=models.ForeignKey(Student)
    courseID=models.ForeignKey(Course)
    hwNo=models.IntegerField()
    taskNo=models.IntegerField()
    date=models.DateTimeField()
    result=models.IntegerField()

class Achievement(models.Model):
    achievement=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

class AchievedAchievement(models.Model):
    achievementID=models.ForeignKey(Achievement)
    studentID=models.ForeignKey(Student)