"""Users URLs"""
#Utilities
from typing import List, Any
#Django
from django.urls import path

#Views
from users import views

urlpatterns: List[Any] = [ 

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    ),

    path(
        route='logut/',
        view=views.LogoutView.as_view(),
        name='logut',
    ),

    path(
        route='signup',
        view=views.SignUp.as_view(),
        name='signup',
    ),

    path(
        route='user/',
        view=views.AccountInformation.as_view(),
        name='information',
    ),

    path(
        route='user/update',
        view=views.UpdateAccountView.as_view(),
        name='update',
    ),
]
