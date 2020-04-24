from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Parkapp import views as v

urlpatterns = [
    path('', views.home, name='home-url'),
    path("register/", v.register, name="register"),
    #path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Parkapp/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Parkapp/home.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('username_change/', views.UsernameChangeView , name='username_change'),
    path('username_change/change_name', views.ChangeName , name='change_name'),
    path('sendmail/', auth_views.LoginView.as_view(template_name='Parkapp/sendmail.html'), name='sendmail'),
    #ath('register/', auth_views.register.as_view(template_name='Parkapp/register.html'), name='register')
]
