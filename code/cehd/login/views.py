from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'login/login.html')

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