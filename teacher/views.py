from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from teacher.forms import TeacherRegistrationForm

def registration(request):
    if request.method == 'POST':
        teacher_data_form = TeacherRegistrationForm(request.POST)
        if teacher_data_form.is_valid():
            teacher_data_form.save()
        return redirect(homepage)
    else:
        teacher_data_form = TeacherRegistrationForm()
    return render(request, 'teacher/registration.html', {
        'teacher_data_form': teacher_data_form,
    })

def homepage(request):
    return render(request, 'teacher/homepage.html')