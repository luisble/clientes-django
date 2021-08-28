from django.shortcuts import redirect, render
from django.contrib.auth import (
    authenticate, 
    login as django_login,
    logout as django_logout
)
from django.contrib import messages
# Create your views here.
def login(request):
    return render(request, "login.html")

def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuario/Senha inválido. Por favor, tente novamente")
    return redirect("index")

def logout(request):
    django_logout(request)
    return redirect("login")