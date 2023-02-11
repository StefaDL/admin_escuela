from django.db import models

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    num_alumn = models.IntegerField()
    anio_lec = models.IntegerField()
    descripcion = models.TextField()

