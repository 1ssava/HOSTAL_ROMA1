from django.shortcuts import render, redirect
from .forms import CustomUserForm

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia 'home' por la vista a la que quieras redirigir tras el login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})