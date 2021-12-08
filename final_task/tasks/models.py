from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=150)
    grades = models.CharField(max_length=150)
    average_grade = models.FloatField()
