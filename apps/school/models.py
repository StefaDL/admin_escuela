from django.db import models

class Auto(models.Model):
    quimica = models.AutoField(primary_key=True)
    fisica = models.TextField()
    ingles = models.TextField()
    matematicas = models.IntegerField()
    lenjuaje = models.TextField()
