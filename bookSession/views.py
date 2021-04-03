from datetime import time
from django.db.models.fields import TimeField
from bookSession.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from child.models import *
from teacher.models import *

from bookSession.forms import SessionForm, timeSlotsForm
# Create your views here.


#  --- both teacher and child
def mySessions(request):
    Session = Session.objects.filter(creationDate=timezone.now()).order_by('published_date')
    return render(request, 'bookSession/mySessions.html',  {'Session': Session})

def cancelSession(request, id):
    obj=Session.objects.get(sessionID=id)
    obj.delete()
    return render(request, 'bookSession/mySessions.html')

def singleSession(request):
    return render(request, 'bookSession/singleSession.html')

def mySlots(request):
    slots = timeSlots.objects.filter(slotDate=timezone.now()).order_by('slotDate')
    return render(request, 'bookSession/mySlots.html', {'slots': slots})

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
            child_session_form.user = request.user
            child_session_form.save()
            return redirect('book_session')
    else:
        child_session_form = SessionForm()
    return render(request, 'bookSession/bookSession.html', {'child_session_form' : child_session_form,})