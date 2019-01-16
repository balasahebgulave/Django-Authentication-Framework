from django.shortcuts import render, redirect
from user_login.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# custom View for SignUp


def home(request):
    return render (request , 'base.html')



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})