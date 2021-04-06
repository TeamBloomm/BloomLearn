from django.db import models
from djongo import models
from django.conf import settings
from child.models import *
from teacher.models import *
from datetime import timedelta

class timeSlots(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
    teacher= models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    startTime=models.TimeField()
    endTime=models.TimeField()
    slotDate = models.DateField()

    def __str__(self):
        title = 'Book Slot on: ' + str(self.slotDate) + ' at: ' + str(self.startTime)
        return title

class Session(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50,)
    duration = models.DurationField(default=timedelta(minutes=40))
    sessionDate = models.DateTimeField()
    # isConfirmed = models.BooleanField()
    # isRejected = models.BooleanField()
    # isCompleted=models.BooleanField()
    sessionUrl = models.URLField(max_length=200)
    sessionID = models.CharField(max_length=100)
    creationDate = models.DateTimeField(auto_now_add=True,)
    slot = models.ForeignKey(timeSlots, on_delete=models.CASCADE)
    teacher= models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    appointmentWith=models.ForeignKey(ChildData, on_delete=models.CASCADE) #child