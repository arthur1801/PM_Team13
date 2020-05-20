from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.contrib.auth.models import User,Group,GroupManager
from django.contrib import messages
from django import forms
from .forms import RegisterForm,RegisterChildForm,ChangeUsernameForm,UserUpdateForm,ProfileUpdateForm,SearchForm
from .forms import SendmailForm
from .models import B7data,Parkimg,Location,Parent_Childs


def home(request):
    Center=Location(31.267509,34.789512)
    South = Location(31.225185, 34.789512)
    North = Location(31.309833, 34.789512)
    CenterWest = Location(31.267509, 34.842315)
    CenterEast = Location(31.267509,34.738301)
    SouthWest = Location(31.225185,34.842315)
    SouthEast = Location(31.225185,34.738301)
    NorthWest = Location(31.309833,34.842315)
    NorthEast = Location(31.309833,34.738301)
    NE = list()
    NW= list()
    SE = list()
    SW = list()
    for i in (B7data.objects.all()):

        if ((i.lon <= North.lon ) and (i.lon>= NorthEast.lon)) and ((i.lat <=North.lat) and (i.lat>=Center.lat)):
            NE.append(i)

        elif ((i.lon <= NorthWest.lon ) and (i.lon>= North.lon)) and ((i.lat <=North.lat) and (i.lat>=Center.lat)):
            NW.append(i)

        elif ((i.lon <= South.lon ) and (i.lon>= SouthEast.lon)) and ((i.lat <=Center.lat) and (i.lat>=South.lat)):
            SE.append(i)

        elif ((i.lon <= SouthWest.lon ) and (i.lon>= South.lon)) and ((i.lat <=Center.lat) and (i.lat>=South.lat)):
            SW.append(i)


    context={
        'parks': NE+NW+SE+SW ,
        'parks-img': Parkimg.objects.all()
    }
    return render(request,'Parkapp/home.html',context)



def login(request):
   return render(request,'Parkapp/login.html')


def PasswordChangeView (request):
    return render(request,'Parkapp/password_change_form.html')


def UsernameChangeView (request):
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            newusername=form.cleaned_data['username']
            user = User.objects.get(username=request.user)
            user.username = newusername
            user.save()
            return redirect('home-url')
    else:
        form = ChangeUsernameForm()

    return render(request,'Parkapp/username_change.html',{'form':form})


def Register (request):
    return render(request,'Parkapp/register.html')
def RegisterChild (request):
    return render(request,'Parkapp/registerChild.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            checkgroup=form.cleaned_data['group']
            print(checkgroup)
            if str(checkgroup).__eq__('parents'):
                my_group = Group.objects.get(name='parents')
            else:
                my_group = Group.objects.get(name='kids')
            form.save()
            idG=User.objects.get_by_natural_key(form.cleaned_data['username'])
            my_group.user_set.add(idG)

            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "Parkapp/register.html", {"form":form})

def registerChild(response):
    if response.method == "POST":
        form = RegisterChildForm(response.POST)
        if form.is_valid():
            my_group = Group.objects.get(name='kids')
            form.save()
            idG=User.objects.get_by_natural_key(form.cleaned_data['username'])
            my_group.user_set.add(idG)
            par=response.user.username
            p=Parent_Childs(Parent_Username=par,Child_Username=idG)
            p.save()
            return redirect("/")
    else:
        form = RegisterChildForm()
    return render(response, "Parkapp/register.html", {"form":form})

def sendmail(request):
    if request.method == 'POST':
        form = SendmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            To_email = form.cleaned_data['To_email']
            message = form.cleaned_data['message']
            try:
                #sm(subject, message, To_email, ['b7parks@gmail.com'])
                sm(subject, message ,'b7parks@gmail.com' ,[To_email],fail_silently=False )
            except :
                return HttpResponse('Invalid header found.')
            return render(request, "Parkapp/success.html", {'some_flag': True})
            #return redirect('profile')

    else:
        form = SendmailForm()

    return render(request, "Parkapp/sendmail.html", {'form': form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'Parkapp/profile.html', context)

def search(request):
    form = SearchForm(request.POST)
    query = request.GET.get('srh', '')
    if query:
        queryset = User.objects.filter(username__contains=query)
    else:
        queryset = []
    return render(request, 'Parkapp/search.html', {'queryset': queryset, })

