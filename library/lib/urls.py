from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginn,name='login'),
    path("signup/",views.signup,name="signup"),
    path('logout/',views.logoutt,name="logout"),
]