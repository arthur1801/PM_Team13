from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.contrib.auth.models import User
from django import forms
from .forms import RegisterForm


def home(request):
    return render(request,'Parkapp/home.html')

def login(request):
    return render(request,'Parkapp/login.html')

def PasswordChangeView (request):
    return render(request,'Parkapp/password_change_form.html')


def UsernameChangeView (request):
    return render(request,'Parkapp/username_change.html')


def Register (request):
    return render(request,'Parkapp/register.html')

def ChangeName (request):
    #if request.method == "POST":
        #newusername = request.POST["newusername"]
        #if User.objects.filter(username=newusername).exists():
        #raise forms.ValidationError(u'Username "%s" is not available.' % newusername)

    user = User.objects.get(username="test")
    user.username = "test1"
    user.save()

    return home
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "Parkapp/register.html", {"form":form})

def send_mail(request):
    res = sm(
        subject = 'Subject here',
        message = 'Here is the message.',
        from_email = 'mail@gmail.com',
        recipient_list = ['someone@example.com'],
        fail_silently=False,
    )

    return HttpResponse(f"Email sent to {res} members")
    #return HttpResponse("Email sent to "+ res +" members")