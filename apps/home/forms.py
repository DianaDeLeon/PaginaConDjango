from django import forms
from .models import EstudiantePublica, EstudianteAutoriza, Articulos,Publicaciones,Comentarios

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