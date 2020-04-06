from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-url'),
    path('login/', views.login, name='login-url'),

]