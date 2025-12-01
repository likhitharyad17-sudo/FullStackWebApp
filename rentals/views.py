from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import BookingForm
from django.urls import reverse

def home(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'rentals/home.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.save()
            # mark car unavailable for simplicity
            car.available = False
            car.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'rentals/car_detail.html', {'car': car, 'form': form})

def booking_success(request):
    return render(request, 'rentals/booking_success.html')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to CarConnect.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'rentals/register.html', {'form': form})

