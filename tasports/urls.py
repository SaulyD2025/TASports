from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginview, name='login'),
    path('register', views.register, name='register'),
    path('teamselection', views.teamselection, name='teamselection'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings', views.delete, name='settings')
]