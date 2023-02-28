from django.db import models

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    num_alumn = models.IntegerField()
    anio_lec = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    id_docente = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=65)
    apellido = models.CharField(max_length=65)
    materia = models.ForeignKey(Materia, null=False, on_delete=models.CASCADE)
