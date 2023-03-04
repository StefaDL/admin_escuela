from django.contrib import admin
from . import models

admin.site.register(models.Materia)
admin.site.register(models.Docente)
admin.site.register(models.Estudiante)