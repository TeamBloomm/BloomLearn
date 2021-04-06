from django.urls import path
from .  import views

# Create your views here.
app_name = "bookSession"
urlpatterns = [
    path('addSession/', views.addSession, name='addSession'),
    path('createSession/', views.createSession, name='createSession'),
    path('cancelSession/', views.cancelSession, name='cancelSession'),
    path('mySessions/', views.mySessions, name='mySessions'),
    path('singleSession/', views.singleSession, name='singleSession'),
    path('mySlots/', views.mySlots, name='mySlots'),
    path('singleS/', views.singleS, name='singleS'),
]