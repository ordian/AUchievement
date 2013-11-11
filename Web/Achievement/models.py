from django.db import models

#example
class Achievement(models.Model):
  tasks_to_solve = models.IntegerField()
  text = models.CharField(max_length=200)