from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import EstudiantePForm, EstudianteAForm, ArticulosForm, PublicacionesForm, ComentariosForm, RegistroForm
from django.urls import reverse_lazy
from .models import Usuario
from django.contrib.auth.views import LoginView
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class ArticuloView(TemplateView):
    template_name='articulos.html'

class PublicacionView(TemplateView):
    template_name='publicacion.html'

class ComentarioView(TemplateView):
    template_name='comentario.html'


class AcercadeView(TemplateView):
    template_name='acercade.html'



class CrearEstudiantePView(CreateView):
    template_name="crearEstudiante.html"
    form_class=EstudiantePForm
    success_url= reverse_lazy('home:homeapp')

class CrearEstudianteAView(CreateView):
    template_name="crearEstudianteAu.html"
    form_class=EstudianteAForm
    success_url= reverse_lazy('home:homeapp')

class CrearArticuloView(CreateView):
    template_name="crearArticulo.html"
    form_class=ArticulosForm
    success_url= reverse_lazy('home:homeapp')

class CrearPublicacionesView(CreateView):
    template_name="crearPublicacion.html"
    form_class=PublicacionesForm
    success_url= reverse_lazy('home:homeapp')

class CrearComentariosView(CreateView):
    template_name="crearComentarios.html"
    form_class=ComentariosForm
    success_url= reverse_lazy('home:homeapp')


class RegistroView(CreateView):
    model=Usuario
    form_class=RegistroForm
    success_url= reverse_lazy('home:homeapp')

class  LoginView(LoginView):
    template_name='login.html'
    