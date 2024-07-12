from django import forms
from .models import Habitacion, Hostal

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
