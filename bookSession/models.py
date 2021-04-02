from django.db import models
from django import forms
from djongo import models
from django.conf import settings
from child.models import *
from teacher.models import *

class Slots(models.Model):
    dateAvailable = models.DateTimeField()
    teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    available = models.BooleanField()
    sessions = models.ForeignKey('Session', on_delete=models.CASCADE)


    def createSlots(self):
        self.published_date = timezone.now()
        self.save()

# class slotChoices(datetime.date, models.Choices):
#     available = models.BooleanField()

class Session(models.Model):
    title = models.CharField(max_length=50,)
    duration = models.DurationField()
    sessionDate = models.DateTimeField(default=timezone.now)
    child = models.ForeignKey(ChildData, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    sessionUrl = models.URLField(max_length=200)
    # slot = models.DateField()
    booking_status = models.BooleanField()
    booking_id = models.CharField(max_length=100, blank=True,)
    creationDate = models.DateTimeField(auto_now_add=True,)
    slot = models.ForeignKey('Slots', on_delete=models.CASCADE)

    #     def baby_boomer_status(self):
    #     "Returns the person's baby-boomer status."
    #     import datetime
    #     if self.birth_date < datetime.date(1945, 8, 1):
    #         return "Pre-boomer"
    #     elif self.birth_date < datetime.date(1965, 1, 1):
    #         return "Baby boomer"
    #     else:
    #         return "Post-boomer"

    # @property
    # def full_name(self):
    #     "Returns the person's full name."
    #     return '%s %s' % (self.first_name, self.last_name)

    def childBook(self):
        # self.published_date = timezone.now()
        self.save()

    # def 

    def __str__(self):
        return self.title