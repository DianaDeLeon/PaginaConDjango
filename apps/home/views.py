from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class ListadoView(TemplateView):
    template_name='listado.html'