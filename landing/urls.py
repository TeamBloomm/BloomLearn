from django.urls import path
from .  import views

# Create your views here.
app_name = "landing"
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('role/', views.select_role, name='select_role'),
]