from django.db import models
from djongo import models
from django.conf import settings
from child.models import *
from teacher.models import *
from datetime import timedelta

class Session(models.Model):
    title = models.CharField(max_length=50,)
    duration = models.DurationField(default=timedelta(minutes=60))
    sessionDate = models.DateField()
    sessionTime = models.TimeField()
    status = models.BooleanField()
    child = models.ForeignKey(ChildData, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    sessionUrl = models.URLField(max_length=200)
    sessionID = models.CharField(max_length=100, blank=True,)
    creationDate = models.DateTimeField(auto_now_add=True,)

    # def createSlots(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def bookSession(self):
        self.creationDate = timezone.now()
        self.save()

    # def 

    def __str__(self):
        return self.title