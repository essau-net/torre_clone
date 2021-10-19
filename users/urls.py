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
        route='user/',
        view=views.AccountInformation.as_view(),
        name='information'
    ),
    
    # path(
    #     route='/user/update',
    #     view=views.UpdateView.as_view(),
    #     name='update'
    # ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    ),

    path(
        route='signup',
        view=views.SignUp.as_view(),
        name='signup',
    )
]
