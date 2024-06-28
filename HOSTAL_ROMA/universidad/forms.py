from django import forms
from .models import Universidad

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = ['direccion', 'nombre']
