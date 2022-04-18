from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import IndexForm
from .models import Airport, FlightSchedule

def home(request):
    print("in home view")
    if request.method == 'POST':
        print("inside post method")
        form = IndexForm(request.POST)
        if form.is_valid():
            print("inside valid")
            departure_airport = form.cleaned_data.get('from_place')
            arrival_airport = form.cleaned_data.get('to_place')
            date = form.cleaned_data.get('date')
            print(departure_airport)
            print(arrival_airport)
            print(date)
            queryset = FlightSchedule.objects.select_related('flight').filter(flight__departure__id = departure_airport, flight__arrival__id = arrival_airport, departureTime = date)
            print(queryset)
            # return redirect('home', {'queryset':queryset})
            return render(request, 'flight_list.html', {'queryset':queryset})
        
    else:
        print("inside get method")
        form = IndexForm()
        airports = Airport.objects.all()
        context = {'airports':airports, 'form':form}
        return render(request, 'index.html', context)


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

# def searchFlight(request):
#     if request.method == 'POST':
#         form = IndexForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('list/')

#     else:
#         form = IndexForm()
#     return render(request, 'index.html', {'form':form})    