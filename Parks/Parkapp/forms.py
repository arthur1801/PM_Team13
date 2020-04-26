from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    Above_12= forms.BooleanField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","Above_12"]

class ChangeUsernameForm(UserChangeForm ):
    password = None
    class Meta:
        model = User
        fields = ["username"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
