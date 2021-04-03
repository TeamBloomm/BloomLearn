from bookSession.models import Session
from django.shortcuts import render, redirect
from child.models import *
from teacher.models import *

from bookSession.forms import SessionForm
# Create your views here.

#  --- both teacher and child
def mySessions(request):
    return render(request, 'bookSession/mySessions.html')

def cancelSession(request):
    return render(request, 'bookSession/cancelSession.html')

def singleSession(request):
    return render(request, 'bookSession/singleSession.html')


def createSession(request):
    if request.method == "POST":
        child_session_form = SessionForm(request.POST)
        if child_session_form.is_valid():
            child_session_form.save()
            return redirect('bookSession:singleSession')
    else:
        child_session_form = SessionForm()
    return render(request, 'bookSession/createSession.html', {'child_session_form' : child_session_form,})

# --- child features
def addSession(request):
    return render(request, 'bookSession/bookSession.html')



# def bookedSession(request):
#    if "user" in request.session:
#        appointments=client.query(q.paginate(q.match(q.index("events_today_paginate"), request.session["user"]["username"],str(datetime.date.today()))))["data"]
#        appointments_count=len(appointments)
#        page_number = int(request.GET.get('page', 1))
#        appointment = client.query(q.get(q.ref(q.collection("Events"), appointments[page_number-1].id())))["data"]
#        context={"count":appointments_count,"appointment":appointment,"page_num":page_number, "next_page": min(appointments_count, page_number + 1), "prev_page": max(1, page_number - 1)}
#        return render(request,"today-appointment.html",context)
#    else:
#        return HttpResponseNotFound("Page not found")