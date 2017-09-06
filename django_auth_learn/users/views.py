from django.shortcuts import render, redirect
from users.forms import RegisterForm
# Create your views here.

from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})