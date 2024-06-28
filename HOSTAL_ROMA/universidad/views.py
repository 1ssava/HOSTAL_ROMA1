from django.shortcuts import render, redirect
from .models import Universidad
from .forms import UniversidadForm

def universidad_list(request):
    universidades = Universidad.objects.all()
    return render(request, 'universidad_list.html', {'universidades': universidades})

def universidad_create(request):
    if request.method == 'POST':
        form = UniversidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('universidad')
    else:
        form = UniversidadForm()
    return render(request, 'universidad.html', {'form': form})
        