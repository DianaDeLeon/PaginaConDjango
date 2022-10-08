from django import forms
from .models import EstudiantePublica, EstudianteAutoriza, Articulos,Publicaciones,Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EstudiantePForm(forms.ModelForm):
    class Meta:
        model=EstudiantePublica
        fields = '__all__'

class EstudianteAForm(forms.ModelForm):
    class Meta:
        model=EstudianteAutoriza
        fields = '__all__'

class ArticulosForm(forms.ModelForm):
    class Meta:
        model=Articulos
        fields = '__all__'

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model=Publicaciones
        fields = '__all__'

class ComentariosForm(forms.ModelForm):
    class Meta:
        model=Comentarios
        fields = '__all__'

class RegistroForm(UserCreationForm):
    first_name=forms.CharField(max_length=140,required=True)
    last_name=forms.CharField(max_length=140,required=False) 
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

