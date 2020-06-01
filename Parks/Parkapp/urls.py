from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Parkapp import views as v
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home-url'),
    path("register/", v.register, name="register"),
    path("registerChild/", v.registerChild, name="registerChild"),
    path('login/', auth_views.LoginView.as_view(template_name='Parkapp/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Parkapp/home.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('username_change/', views.UsernameChangeView , name='username_change'),
    path('sendmail/',v.sendmail,name='sendmail'),
    path('profile/',v.profile,name='profile'),
    path('search/',v.search,name='search'),
    path('assignChild/',v.assignChild,name='assignChild'),
    path('searchpark/',v.searchPark,name='searchPark'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)