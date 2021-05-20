from datetime import time
from django.db.models.fields import TimeField
from bookSession.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from child.models import *
from teacher.models import *
from datetime import datetime as dt

from bookSession.forms import SessionForm, timeSlotsForm
# Create your views here.
from pyzoom import ZoomClient
client = ZoomClient('DoqYmeizR3SCqhaOWllLZw', 'u77RUz9zNcmwyaQx9g4a9K9oZCCDXNK7EaBk')

#  --- both teacher and child
def mySessions(request):
    sessions = Session.objects.filter(creationDate=timezone.now()).order_by('title')
    return render(request, 'bookSession/mySessions.html',  {'sessions': sessions})

def cancelSession(request, id):
    obj=Session.objects.get(sessionID=id)
    obj.delete()
    return render(request, 'bookSession/mySessions.html')

def singleSession(request):
    return render(request, 'bookSession/singleSession.html')

def singleS(request):
    return render(request, 'bookSession/singleS.html')

def mySlots(request):
    # slots = timeSlots.objects.all()
    # slot = {"slots": slots}
    # return render_to_response("login/profile.html", stu)
    slots = timeSlots.objects.filter(slotDate=timezone.now()).order_by('slotDate')
    return render(request, 'bookSession/mySlots.html',{'slots': slots})

#  --- teacher features
def createSession(request): # creating a new slot
    if request.method == "POST":
        tform =timeSlotsForm(request.POST)
        if tform.is_valid():
            slot = tform.save(commit=False)
            slot.user = request.user
            slot.save()
            return render(request, 'bookSession/singleSession.html', {'slot' :slot,})
    else:
        tform = timeSlotsForm()
    return render(request, 'bookSession/createSession.html', {'tform' :tform,})

# --- child features
def addSession(request): #book session
    if request.method == "POST":
        child_session_form = SessionForm(request.POST)
        if child_session_form.is_valid():
            session = child_session_form.save(commit=False)
            session.sessionURL = client.meetings.create_meeting('Auto created 1', start_time=dt.now().isoformat(), duration_min=40, password='not-secure')
            session.user = request.user
            session.save()
            return render(request, 'bookSession/singleS.html', {'session' :session,})
    else:
        child_session_form = SessionForm()
    return render(request, 'bookSession/bookSession.html', {'child_session_form' : child_session_form,})