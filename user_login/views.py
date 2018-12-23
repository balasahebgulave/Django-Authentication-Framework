from django.shortcuts import render
from user_login.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# custom View for SignUp
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password2']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            form.save()
            return HttpResponseRedirect('register')

    else: 
        form = UserForm()
    return render (request , 'base.html' , {'form':form})

# django model for SignUp

# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('register')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# Create your views here.
