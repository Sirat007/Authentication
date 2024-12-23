from django.shortcuts import render, redirect
from .forms import SignUpForm, ChangeUserDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.



def home(request):
    return render(request,'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,"Account Created succesfully")
                form.save()

        else:
            form = SignUpForm()

        return render(request,'signup.html',{ 'form' : form})
    
    else:
        return redirect('homepage')
    

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name,password = userpass)
                if user is not None:
                    messages.success(request,"Logged in successfully")
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('homepage')

def edit(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST,instance = request.user)
            if form.is_valid():
                messages.success(request,"Updated successfully")
                form.save()
        
        else:
            form = ChangeUserDataForm(instance = request.user)
        return render(request,'edit.html',{'form':form})
    else:
        return redirect('homepage')
    

def userlogout(request):
    messages.success(request,"Logged out successfully")
    logout(request)
    return redirect('homepage')

def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request,"Password Updated")
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'pass_change.html',{'form':form})
    else:
        return redirect('login')
    
def changepass_2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request,"Password Updated")
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'changepass.html',{'form':form})
    else:
        return redirect('login')