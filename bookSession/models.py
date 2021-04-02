from django.db import models
from django import forms
from djongo import models
from django.conf import settings
from child.models import *
from teacher.models import *

class Slots(models.Model):
     available = models.IntegerField()
     timeAvailable = models.IntegerField()
     dayAvailable = models.IntegerField()
     teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)

     def createSlots(self):
        self.published_date = timezone.now()
        self.save()

class Session(models.Model):
    title = models.CharField(max_length=200)
    sessionDate = models.DateTimeField(default=timezone.now)
    child = models.ForeignKey(ChildData, on_delete=models.CASCADE)
    sessionUrl = models.DateTimeField(blank=True, null=True)
    slot = models.DateField()


    def childBook(self):
        # self.published_date = timezone.now()
        self.save()

    # def 

    def __str__(self):
        return self.title