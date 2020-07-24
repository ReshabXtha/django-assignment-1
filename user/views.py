from django.contrib.auth import get_user_model, authenticate, login, logout
from Blog import backend
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import SignUpForm, LoginForm

USER = get_user_model()


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("do not match")
    elif request.method == "GET":
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = USER(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/user/login/')
    elif request.method == "GET":
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/user/login/')
