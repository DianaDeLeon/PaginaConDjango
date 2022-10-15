from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView
from .forms import EstudiantePForm, EstudianteAForm, ArticulosForm, PublicacionesForm, ComentariosForm, RegistroForm
from django.urls import reverse_lazy
from .models import Usuario, EstudianteAutoriza,EstudiantePublica,Articulos,Comentarios, Publicaciones
from django.contrib.auth.views import LoginView
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class AcercadeView(TemplateView):
    template_name='acercade.html'

#class EstudiantesView(ListView):
#    template_name='estudiantes.html'

#class AdministradoresView(TemplateView):
#    template_name='administradores.html'

#class ArticuloView(TemplateView):
#    template_name='articulos.html'

#class PublicacionView(TemplateView):
#    template_name='publicacion.html'

#class ComentarioView(TemplateView):
#    template_name='comentario.html'




class EstudiantesView(ListView):
    template_name='estudiantes.html'
    model = EstudiantePublica

    def get_query(self):
        return EstudiantePublica.objects.all()

class AdministradoresView(ListView):
    template_name='administradores.html'
    model= EstudianteAutoriza

    def get_query(self):
        return EstudianteAutoriza.objects.all()

class ArticuloView(ListView):
    template_name='articulos.html'
    model = Articulos

    def get_query(self):
        return Articulos.objects.all()

class PublicacionView(ListView):
    template_name='publicacion.html'
    model = Publicaciones

    def get_query(self):
        return Publicaciones.objects.all()

class ComentarioView(ListView):
    template_name='comentario.html'
    model = Comentarios

    def get_query(self):
        return Comentarios.objects.all()


#class AcercadeView(TemplateView):
#    template_name='acercade.html'


class CrearEstudiantePView(CreateView):
    template_name="crearEstudiante.html"
    form_class=EstudiantePForm
    success_url= reverse_lazy('home:estudiantesapp')

class CrearEstudianteAView(CreateView):
    template_name="crearEstudianteAu.html"
    form_class=EstudianteAForm
    success_url= reverse_lazy('home:administradoresapp')

class CrearArticuloView(CreateView):
    template_name="crearArticulo.html"
    form_class=ArticulosForm
    success_url= reverse_lazy('home:articulosapp')

class CrearPublicacionesView(CreateView):
    template_name="crearPublicacion.html"
    form_class=PublicacionesForm
    success_url= reverse_lazy('home:publicacionapp')

class CrearComentariosView(CreateView):
    template_name="crearComentarios.html"
    form_class=ComentariosForm
    success_url= reverse_lazy('home:comentarioapp')


class RegistroView(CreateView):
    model=Usuario
    form_class=RegistroForm
    success_url= reverse_lazy('home:homeapp')

class  LoginView(LoginView):
    template_name='login.html'
    