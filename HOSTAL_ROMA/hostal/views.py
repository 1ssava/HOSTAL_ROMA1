from django.shortcuts import render, redirect
from .forms import HabitacionForm, HostalForm

def home(request):
    return render(request, 'home.html')

def habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habitacion')
    else:
        form = HabitacionForm()
    return render(request, 'habitacion.html', {'form': form})

def hostal(request):
    if request.method == 'POST':
        form = HostalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostal')
    else:
        form = HostalForm()
    return render(request, 'hostal.html', {'form': form})
