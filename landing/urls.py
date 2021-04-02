from django.urls import path
from .  import views

# Create your views here.
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]