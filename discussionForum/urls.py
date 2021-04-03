from django.contrib import admin
from django.urls import path
from discussionForum import views

app_name = 'discussionForum'
urlpatterns = [
    path('', views.home,name='home'),
    path('addInForum/',views.addInForum, name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
]