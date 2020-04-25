from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    Above_12= forms.BooleanField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","Above_12"]