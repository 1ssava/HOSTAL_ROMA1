from django.shortcuts import render, redirect
from .forms import HabitacionForm, HostalForm, ContactForm, EmployeeForm
from django.http import HttpResponse

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

def home(request):
    return render(request, 'home_final.html')

def widget(request):
    if request.method == 'GET':    
         form = ContactForm()
         return render(request, 'widget.html', {'form': form})

    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): 
            # Aqui irian todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Valido")
        else:
            # Aqui comunicamos que los datos no son validos
            return render(request, 'widget.html', {'form': form})
        
def formsMod(request):
    form = EmployeeForm()
    return render(request, 'formsMod.html', {'form': form})