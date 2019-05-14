from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# forms
from .forms import UserUpdateForm, ProfileForm

# Create your views here.

# login page
def  login_page(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username = Username, password = Password)

        # check if user is not none
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('dashboard')

            else:
                messages.error(request, 'Disabled Account')
                return render(request, 'accounts/login.html', {})

        else:
            messages.error(request, 'Invalid Username or Password')
            return render(request, 'accounts/login.html', {})

    else:

        return render(request, 'accounts/login.html', {})


# profile section
def user_profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        # check if form is valid
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Profile Form Updated Successfully')
            return redirect('profile')

    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
        context = {
            'uform':uform,
            'pform':pform,
        }
    return render(request, 'accounts/profile.html', context)

