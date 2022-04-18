from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import IndexForm

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def flight(request):
    return render(request, 'flight.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def searchFlight(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('list/')

    else:
        form = IndexForm()
    return render(request, 'index.html', {'form':form})    