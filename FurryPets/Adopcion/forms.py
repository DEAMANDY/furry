from django import forms
from .models import Mascotas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}


# Creacion de el formulario para publicar mascotas.
class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = ['nombre','tipo_mascota','dueño','ciudad','descripcion','foto']


