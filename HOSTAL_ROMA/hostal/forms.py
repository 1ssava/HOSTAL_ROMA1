from typing import Any
from django import forms
from .models import Habitacion, Hostal, Employee

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['num_habitacion', 'tipo_habitacion', 'estado', 'precio', 'fecha_inicio', 'fecha_fin']
    
    def __init__(self, *args, **kwargs):
        super(HabitacionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class HostalForm(forms.ModelForm):
    class Meta:
        model = Hostal
        fields = ['id_habitacion', 'nombre_fantasia', 'rol', 'email', 'direccion', 'telefono']
    
    def __init__(self, *args, **kwargs):
        super(HostalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ContactForm(forms.Form):
    name = forms.CharField( label="Nombre", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_name (self):
        name = self.cleaned_data.get("name")
        if name != "Open":
            raise forms.ValidationError("Tans solo el valor Open esta permitido para este campo")
        else:
            return name
        
class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee
        fields = ['name', 'last_name', 'email']
        #exclude = ('email',)

        