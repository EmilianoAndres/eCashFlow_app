# onboarding/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns for other views if needed
]
