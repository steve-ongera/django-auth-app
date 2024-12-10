from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomRegistrationForm, CustomLoginForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
