import django.contrib.auth.views
from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView, UserLogoutView, Home

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name='logout'),
    path('', Home.as_view(), name='home')
]