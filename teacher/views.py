from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import logout_then_login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render

from teacher.forms import FileUploadForm, TeacherRegistrationForm, UserForm


def details(request):
    if request.method == 'POST':
        teacher_data_form = TeacherRegistrationForm(request.POST)
        if teacher_data_form.is_valid():
            teacher_data_form.save()
            return redirect('teacher:homepage')
        else:
            teacher_data_form = TeacherRegistrationForm()
            return render(request, 'teacher/home.html', {
        'teacher_data_form': teacher_data_form,
        })
    else:
        teacher_data_form = TeacherRegistrationForm()
        return render(request, 'teacher/details.html', {
            'teacher_data_form': teacher_data_form,
        })

def registration(request):
    if request.user.is_authenticated:
        return redirect('teacher:homepage')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user) 
            return redirect('teacher:details')
        else:
            user_form = UserForm()
            return render(request, 'teacher/registration.html', {
                'user_details': user_form,
            })
    else:
        user_form = UserForm()
        return render(request, 'teacher/registration.html', {
            'user_details': user_form,
        })

def homepage(request):
    return render(request, 'teacher/home.html')


def singleCourse(request):
    return render(request, 'teacher/singleCourse.html')

def courseHome(request):
    return render(request, 'teacher/courseHome.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('teacher:homepage')
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('teacher:homepage')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'teacher/signin.html',{'form': form})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'teacher/signin.html',{'form': form})


def signout(request):
    return logout_then_login(request, login_url='/teacher/sign-in')

def simple_upload(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()#commit=False)
            return redirect('teacher:courseHome')
    else:
        file_form = FileUploadForm()
    return render(request, 'teacher/simple_upload.html', {
        'file_form': file_form
    })
