"""ColegioAmigos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import HomeView,EstudiantesView,AdministradoresView,AcercadeView,ArticuloView,PublicacionView,ComentarioView, RegistroView, LoginView
from .views import CrearEstudiantePView,CrearEstudianteAView,CrearArticuloView,CrearPublicacionesView,CrearComentariosView
from .views import EditarEstudiantePView, EditarArticuloView,EditarComentariosView,EditarEstudianteAView,EditarPublicacionesView
from .views import  DetalleEstudiantesView, DetalleEstudianteAView, DetalleArticuloView, DetalleComentariosView, DetallePublicacionesView


from apps.home import views

app_name='home'
urlpatterns = [
   path('', LoginView.as_view(), name ='login'),
   path('inicio/',HomeView.as_view(), name='homeapp'),
   path('estudiantes/', EstudiantesView.as_view(), name='estudiantesapp'),
   path('administradores/',AdministradoresView.as_view(), name='administradoresapp'),
   path('articulos/',ArticuloView.as_view(), name='articulosapp'),
   path('publicacion/',PublicacionView.as_view(), name='publicacionapp'),
   path('comentario/',ComentarioView.as_view(), name='comentarioapp'),
   path('acercade/',AcercadeView.as_view(), name='acercadeapp'),

   path('crearEP/',CrearEstudiantePView.as_view(), name='crearestudiantep'),
   path('crearEA/',CrearEstudianteAView.as_view(), name='crearestudiantea'),
   path('crearArticulo/',CrearArticuloView.as_view(), name='creararticulo'),
   path('crearPublicacion/',CrearPublicacionesView.as_view(), name='crearpublicacion'),
   path('crearComentario/',CrearComentariosView.as_view(), name='crearcomentarios'),

   path('registrar/',RegistroView.as_view(), name='registro'),

   path('editarEP/<int:pk>/',EditarEstudiantePView.as_view(), name='editarestudiantep'),
   path('editarEA/<int:pk>/',EditarEstudianteAView.as_view(), name='editarestudiantea'),
   path('editarArticulo/<int:pk>/',EditarArticuloView.as_view(), name='editararticulo'),
   path('editarPublicacion/<int:pk>/',EditarPublicacionesView.as_view(), name='editarpublicacion'),
   path('editarComentario/<int:pk>/',EditarComentariosView.as_view(), name='editarcomentarios'),

   path('detalleEP/<int:pk>/', DetalleEstudiantesView.as_view(), name='detalleestudiante'),
   path('detalleEA/<int:pk>/', DetalleEstudianteAView.as_view(), name='detalleestudianteA'),
   path('detalleArticulo/<int:pk>/', DetalleArticuloView.as_view(), name='detallearticulo'),
   path('detallePublicacion/<int:pk>/', DetallePublicacionesView.as_view(), name='detallepublicacion'),
   path('detalleComentario/<int:pk>/', DetalleComentariosView.as_view(), name='detallecomentario'),
]
