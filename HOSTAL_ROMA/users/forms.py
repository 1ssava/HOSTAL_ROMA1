from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=True, label='Nombre de Usuario: ')
    first_name = forms.CharField(max_length=15, required=True, label='Nombre')
    last_name = forms.CharField(max_length=15, required=True, label='Apellido')
    email = forms.EmailField(max_length=30, help_text='Ingrese un correo electrónico válido.', required=True, label='Correo Electrónico')

    # Validador para solo permitir números
    numeric = RegexValidator(r'^[0-9+]+$', 'Ingrese solo números válidos.')

    phone_number = forms.CharField(
        validators=[numeric],
        max_length=12,
        initial='+569', 
        required=True, 
        label='Teléfono',
        help_text='(Formato: +56912345678)',
        error_messages={'invalid': 'Ingrese un número de teléfono válido que comience con +569 y tenga 9 dígitos después del código de país.'}
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            self.add_error('password1', error)
        return password1


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
