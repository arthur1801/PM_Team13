from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User,Group
from django.forms import ModelForm
from .models import Profile,Parkimg,Parent_Childs



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    Above_12= forms.BooleanField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","Above_12","group"]

class RegisterChildForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

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

class SendmailForm(forms.Form):
    To_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:

        fields = ['To_email','subject','message']


class SearchForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']


class assignChildForm(forms.ModelForm):
    Parent_Username = forms.ModelChoiceField(queryset=(Group.objects.get(name='parents')).user_set.all(), required=True)
    Child_Username = forms.ModelChoiceField(queryset=(Group.objects.get(name='kids')).user_set.all(), required=True)

    class Meta:
        model=Parent_Childs
        fields=['Parent_Username','Child_Username']

