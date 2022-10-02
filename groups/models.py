import email
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length = 100 , null =True)
    age = models.PositiveIntegerField(default=0 , null =True)
    email = models.EmailField(max_length = 254 , null =True)
    group = models.ForeignKey(Group , on_delete = models.SET_NULL , null =True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 100 , null =True)
    age = models.PositiveIntegerField(default=0 , null =True)
    email = models.EmailField(max_length = 254 , null =True)
    group = models.ForeignKey(Group, on_delete = models.SET_NULL , null =True)

    def __str__(self):
        return self.name

