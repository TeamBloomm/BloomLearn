from django.urls import path
from . import views

app_name = 'child'
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('home/', views.homepage, name='homepage'),
    path('details/', views.details, name='details'),
    path('sign-in/', views.signin, name='signin'),
    path('sign-out/', views.signin, name='signout'),
]