from django.shortcuts import render

def home(request):
    return render(request,'Parkapp/home.html')

def login(request):
    return render(request,'Parkapp/login.html')

def PasswordChangeView (request):
    return render(request,'Parkapp/password_change_form.html')
