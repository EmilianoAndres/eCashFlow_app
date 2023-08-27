# onboarding/urls.py
from django.urls import path
from .presentation.api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('secondpage', views.CreateOrderView.as_view(), name='CreateOrderView')
    # Add more URL patterns for other views if needed
]
