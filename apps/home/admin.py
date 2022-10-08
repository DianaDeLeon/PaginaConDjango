from django.contrib import admin
from .models import EstudiantePublica,EstudianteAutoriza,Articulos,Publicaciones,Comentarios,Usuario
# Register your models here.

admin.site.register(EstudiantePublica)
admin.site.register(EstudianteAutoriza)
admin.site.register(Articulos)
admin.site.register(Publicaciones)
admin.site.register(Comentarios)
admin.site.register(Usuario)