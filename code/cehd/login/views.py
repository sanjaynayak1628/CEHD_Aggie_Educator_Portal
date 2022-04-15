from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from . forms import UserRegisterForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.template.defaulttags import register
@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def home(request):
    return render(request, 'login/login.html')

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                userType = request.POST['usertype']
                print(userType)
                return redirect(f'/timelogs/{userType}/email/{username}')
        else:
            messages.error(request,'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('/login/')
        
                
    else:
        form = AuthenticationForm()
    return render(request,'login/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
        else:
            errorMsgDict = form.error_messages
            if errorMsgDict.get('password_mismatch'):
                messages.error(request, errorMsgDict['password_mismatch'])
            return redirect('register')
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

def profile(request):
    return render(request, 'login/profile.html')