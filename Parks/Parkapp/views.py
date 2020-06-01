from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.contrib.auth.models import User,Group,GroupManager
from django.contrib import messages
from django import forms
from .forms import RegisterForm,RegisterChildForm,ChangeUsernameForm,UserUpdateForm,ProfileUpdateForm,SearchForm,assignChildForm
from .forms import SendmailForm
from .models import B7data,Parkimg,Location,Parent_Childs


def home(request):
    return render(request,'Parkapp/home.html')


def searchPark(request):
    SandSurface=list()
    GrassSurface=list()
    RubberSurface=list()
    Shadowing=list()
    Omega=list()
    Combined1= list()
    Combined2= list()
    Combined3= list()
    Swing = list()






    Center = Location(31.267509, 34.789512)
    South = Location(31.225185, 34.789512)
    North = Location(31.309833, 34.789512)
    SouthWest = Location(31.225185, 34.842315)
    SouthEast = Location(31.225185, 34.738301)
    NorthWest = Location(31.309833, 34.842315)
    NorthEast = Location(31.309833, 34.738301)
    NE = list()
    NW = list()
    SE = list()
    SW = list()

    for i in (B7data.objects.all()):
        #surface mapping
        if(i.surface == 'משטח חול'):
            SandSurface.append(i)
        elif(i.surface == 'דשא סינטטי'):
            GrassSurface.append(i)
        else:
            RubberSurface.append(i)

        #shadowing mapping
        if(i.shadowing == 'יש'):
            Shadowing.append(i)

        #omega mapping
        if(i.omega == 1 or i.omega == '1'):
            Omega.append(i)

        #combined1 mapping
        if (i.combined1 >= 1 ):
            Combined1.append(i)
        # combined2 mapping
        if (i.combined2 >= 1 ):
            Combined2.append(i)
        # combined3 mapping
        if (i.combined3 >= 1 ):
            Combined3.append(i)

        #swing mapping
        if (i.Swing >= 1 ):
            Swing.append(i)

        #NE mapping
        if ((i.lon <= North.lon) and (i.lon >= NorthEast.lon)) and ((i.lat <= North.lat) and (i.lat >= Center.lat)):
            NE.append(i)
        #NW mapping
        elif ((i.lon <= NorthWest.lon) and (i.lon >= North.lon)) and ((i.lat <= North.lat) and (i.lat >= Center.lat)):
            NW.append(i)
        #SE mapping
        elif ((i.lon <= South.lon) and (i.lon >= SouthEast.lon)) and ((i.lat <= Center.lat) and (i.lat >= South.lat)):
            SE.append(i)
        #SW mapping
        elif ((i.lon <= SouthWest.lon) and (i.lon >= South.lon)) and ((i.lat <= Center.lat) and (i.lat >= South.lat)):
            SW.append(i)
        filters=list()
        filters.append('Surface-Sand')
        filters.append('Surface-Grass')
        filters.append('Surface-Rubber')
        filters.append('Extreme-Yes')
        filters.append('Combined1-Yes')
        filters.append('Combined2-Yes')
        filters.append('Combined3-Yes')
        filters.append('North East')
        filters.append('North West')
        filters.append('South East')
        filters.append('South West')
        filters.append('Kids with disability')
        filters.append('DayTime Parks')
        filters.append('AllTime Parks')
        filters.append('Recommended age 0-6')
        filters.append('Recommended age 6-10')
        filters.append('Recommended age 10+')


        choose = request.GET.get('choice')

        if choose=='Surface-Sand':
            context = {'parks':SandSurface,
                       'filters':filters}

        elif choose=='Surface-Grass':
            context = {'parks':GrassSurface,
                       'filters':filters}
        elif choose=='Surface-Rubber':
            context = {'parks':RubberSurface,
                       'filters':filters}
        elif choose=='Extreme-Yes':
            context = {'parks':Omega,
                       'filters':filters}
        elif choose=='Combined1-Yes':
            context = {'parks':Combined1,
                       'filters':filters}
        elif choose=='Combined2-Yes':
            context = {'parks':Combined2,
                       'filters':filters}
        elif choose=='Combined3-Yes':
            context = {'parks':Combined3,
                       'filters':filters}
        elif choose=='North East':
            context = {'parks':NE,
                       'filters':filters}
        elif choose=='North West':
            context = {'parks':NW,
                       'filters':filters}
        elif choose=='South East':
            context = {'parks':SE,
                       'filters':filters}
        elif choose=='South West':
            context = {'parks':SW,
                       'filters':filters}
        elif choose=='Kids with disability':
            context = {'parks':RubberSurface+GrassSurface,
                       'filters':filters}
        elif choose=='DayTime Parks':
            context = {'parks':Shadowing,
                       'filters':filters}
        elif choose=='AllTime Parks':
            context = {'parks':NE+NW+SE+SW,
                       'filters':filters}
        elif choose=='Recommended age 0-6':
            context = {'parks':set(RubberSurface)-set(Omega+Combined1+Combined2+Combined3),
                       'filters':filters}
        elif choose=='Recommended age 6-10':
            context = {'parks':set(RubberSurface+GrassSurface)-set(Omega),
                       'filters':filters}
        elif choose=='Recommended age 10+':
            context = {'parks':NE+NW+SE+SW,
                       'filters':filters}





        else:
            context = {
            'filters':filters,
            'parks': None,
            'parks-img': Parkimg.objects.all()
            }
    return render(request, 'Parkapp/searchpark.html',context)

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
            if str(checkgroup).__eq__('parents'):
                my_group = Group.objects.get(name='parents')
            else:
                my_group = Group.objects.get(name='kids')
            form.save()
            if str(checkgroup).__eq__('parents'):
                user = User.objects.get(username=form.cleaned_data['username'])
                user.is_staff = True
                user.save()
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
    set=(Group.objects.get(name='kids')).user_set.all()
    if query:
        queryset = User.objects.filter(username__contains=query)
    else:
        queryset = []
        set=[]
    return render(request, 'Parkapp/search.html', {'set' :set})


def assignChild(request):
    form = assignChildForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Parent=form.cleaned_data['Parent_Username']
            Kid = form.cleaned_data['Child_Username']
            p = Parent_Childs(Parent_Username=Parent, Child_Username=Kid)
            p.save()

    return render(request, 'Parkapp/assignChild.html', {'form': form, })

