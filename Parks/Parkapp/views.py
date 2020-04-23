from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm

def home(request):
    return render(request,'Parkapp/home.html')

def login(request):
    return render(request,'Parkapp/login.html')

def PasswordChangeView (request):
    return render(request,'Parkapp/password_change_form.html')


def UsernameChangeView (request):
    return render(request,'Parkapp/username_change.html')

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