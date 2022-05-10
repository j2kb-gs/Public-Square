# -*- encoding: utf-8 -*-

from django.urls import path
from .views import login_view, register_user, logoutView
#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logoutView, name="logout")
]
