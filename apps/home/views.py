from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView,UpdateView
from django.views.generic.detail import DetailView
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

    def get_queryset(self):
        vnombre =   self.request.GET.get("nombre")
        if(vnombre):
            return EstudiantePublica.objects.filter(nombre__icontains=vnombre)
        else: 
            return EstudiantePublica.objects.all()     

class AdministradoresView(ListView):
    template_name='administradores.html'
    model= EstudianteAutoriza

    def get_queryset(self):
        vnombre =   self.request.GET.get("nombre")
        if(vnombre):
            return EstudianteAutoriza.objects.filter(nombre__icontains=vnombre)
        else: 
            return EstudianteAutoriza.objects.all()

class ArticuloView(ListView):
    template_name='articulos.html'
    model = Articulos

    def get_queryset(self):
        vtitulo =   self.request.GET.get("titulo")
        if(vtitulo):
            return Articulos.objects.filter(titulo__icontains=vtitulo)
        else:
            return Articulos.objects.all()

class PublicacionView(ListView):
    template_name='publicacion.html'
    model = Publicaciones

    def get_queryset(self):
        vtitulo =   self.request.GET.get("titulo")
        if(vtitulo):
            return Publicaciones.objects.filter(articulo__titulo__icontains=vtitulo)
        else:
            return Publicaciones.objects.all()

class ComentarioView(ListView):
    template_name='comentario.html'
    model = Comentarios

    def get_queryset(self):
        vtitulo =   self.request.GET.get("titulo")
        if(vtitulo):
            return Comentarios.objects.filter(articulo__titulo__icontains=vtitulo)
        else:
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
    

class EditarEstudiantePView(UpdateView):
    template_name="editarEstudiante.html"
    model = EstudiantePublica
    form_class=EstudiantePForm
    success_url= reverse_lazy('home:estudiantesapp')

class EditarEstudianteAView(UpdateView):
    template_name="editarEstudianteAu.html"
    model = EstudianteAutoriza
    form_class=EstudianteAForm
    success_url= reverse_lazy('home:administradoresapp')

class EditarArticuloView(UpdateView):
    template_name="editarArticulo.html"
    model = Articulos
    form_class=ArticulosForm
    success_url= reverse_lazy('home:articulosapp')

class EditarPublicacionesView(UpdateView):
    template_name="editarPublicacion.html"
    model = Publicaciones
    form_class=PublicacionesForm
    success_url= reverse_lazy('home:publicacionapp')

class EditarComentariosView(UpdateView):
    template_name="editarComentarios.html"
    model = Comentarios
    form_class=ComentariosForm
    success_url= reverse_lazy('home:comentarioapp')

class DetalleEstudiantesView(DetailView):
    template_name='detalleestudiantes.html'
    queryset = EstudiantePublica.objects.all()
    
class DetalleEstudianteAView(DetailView):
    template_name="detalleestudianteA.html"
    queryset = EstudianteAutoriza.objects.all()

class DetalleArticuloView(DetailView):
    template_name="detallearticulo.html"
    queryset = Articulos.objects.all()

class DetallePublicacionesView(DetailView):
    template_name="detallepublicacion.html"
    queryset = Publicaciones.objects.all()

class DetalleComentariosView(DetailView):
    template_name="detallecomentario.html"
    queryset = Comentarios.objects.all()
