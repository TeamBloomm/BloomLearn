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

    
    # class Meta:
    #     db_table='time_slots'

class Session(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50,)
    duration = models.DurationField(default=timedelta(minutes=60))
    sessionDate = models.DateTimeField()
    # isConfirmed = models.BooleanField()
    # isRejected = models.BooleanField()
    # isCompleted=models.BooleanField()
    sessionUrl = models.URLField(max_length=200)
    sessionID = models.CharField(max_length=100)
    creationDate = models.DateTimeField(auto_now_add=True,)
    teacher= models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    appointmentWith=models.ForeignKey(ChildData, on_delete=models.CASCADE) #child

    # class Meta:
    #     ordering = ['creationDate']
    #     get_latest_by='creationDate'

    # def createSlots(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def bookSession(self):
    #     self.creationDate = timezone.now()
    #     self.save()

    # # def 

    # def __str__(self):
    #     return self.title