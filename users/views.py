from django.shortcuts import render, redirect
from django.contrib.auth import  REDIRECT_FIELD_NAME, login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except :
            messages.error(request, "username does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was successfully logged out!')
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # every skill that doesn't have a description is excluded
    topSkills = profile.skill_set.exclude(description__exact="")
    # every string that doesn't have a description is filterd out
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)