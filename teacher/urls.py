from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('home/', views.homepage, name='homepage'),
    path('details/', views.details, name='details'),
    path('sign-in/', views.signin, name='signin'),
    path('sign-out/', views.signout, name='signout'),
    path('upload/', views.simple_upload, name='simple_upload'),
    path('courseHome/', views.courseHome, name='courseHome'),
    path('singleCourse/', views.singleCourse, name='singleCourse'),
]