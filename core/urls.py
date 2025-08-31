# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # We’ll add about/projects/contact routes later
]
