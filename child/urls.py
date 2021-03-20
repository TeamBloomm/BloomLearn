from django.urls import path
from . import views

app_name = 'child'
urlpatterns = [
    path('register/', views.registration, name='registration'),
]