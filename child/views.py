from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from child.forms import ChildRegistrationForm, GuardianRegistrationForm

def registration(request):
    if request.method == 'POST':
        child_form = ChildRegistrationForm(request.POST)
        if child_form.is_valid():
            child_form.save()
        return render(request, 'child/home.html')
    else:
        child_form = ChildRegistrationForm()
    return render(request, 'child/registration.html', {
        'child_form': child_form,
    })