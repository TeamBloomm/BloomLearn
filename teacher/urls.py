from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('home/', views.homepage, name='homepage')
]