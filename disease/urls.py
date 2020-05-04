from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name="signup"),
    path('index/', views.index, name="index"),
    path('dashboard', views.dashboard, name='dashboard'),
]
