from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import logout_then_login

from child.forms import ChildRegistrationForm, UserForm

def details(request):
    if request.method == 'POST':
        child_data_form = ChildRegistrationForm(request.POST)
        if child_data_form.is_valid():
            child_data_form.save()
            return redirect('child:homepage')
        else:
            print('failed')
            child_data_form = ChildRegistrationForm()
            return render(request, 'child/home.html', {
        'child_data_form': child_data_form,
        })
    else:
        child_data_form = ChildRegistrationForm()
        return render(request, 'child/details.html', {
            'child_data_form': child_data_form,
        })

def registration(request):
    if request.user.is_authenticated:
        return redirect('child:homepage')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user) 
            return redirect('child:details')
        else:
            user_form = UserForm()
            return render(request, 'child/registration.html', {
                'user_details': user_form,
            })
    else:
        user_form = UserForm()
        return render(request, 'child/registration.html', {
            'user_details': user_form,
        })

def homepage(request):
    return render(request, 'child/home.html')

def courseTeachers(request):
    return render(request, 'child/courseTeachers.html')

def courseList(request):
    return render(request, 'child/courseList.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('child:homepage')
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('child:homepage')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'child/signin.html',{'form': form})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'child/signin.html',{'form': form})


def signout(request):
    return logout_then_login(request, login_url='child:signin')