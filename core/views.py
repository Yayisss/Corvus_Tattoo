from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def products(request):
    return render(request, 'core/products.html')

def citas(request):
    return render(request, 'core/citas.html')

def login(request):
    login_required (request)
    return ('registration/login.html')

def exit(request):
    logout(request)
    return redirect('home')


