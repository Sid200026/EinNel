from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'loginsignup/index.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'loginsignup/login.html', {'error':'Wrong Username and Password Combination'})
    return render(request, 'loginsignup/login.html')

def signup(request):
    return render(request, 'loginsignup/signup.html')

def dashboard(request):
    return HttpResponse("You are at dashboard")
