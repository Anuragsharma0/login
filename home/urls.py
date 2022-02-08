from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.signup, name='home'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('dashboard', views.dashboard, name='dashboard')
]