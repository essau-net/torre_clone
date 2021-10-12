"""Users URLs"""
#Utilities
from typing import List, Any
#Django
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

#Views
from users import views

urlpatterns: List[Any] = [
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    ),
]
