from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home-url'),
    #path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Parkapp/login.html'), name='login-url'),

]
