from django.db import models

# Create your models here.

class Computadoras(models.Model):

    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    marca = models.CharField(max_length=60)
    almacenamiento = models.CharField(max_length=60)
    proveedor = models.CharField(max_length=60)

class Celulares(models.Model):

    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    marca = models.CharField(max_length=60)
    almacenamiento = models.CharField(max_length=60)
    proveedor = models.CharField(max_length=60)

class Televisores(models.Model):

    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    marca = models.CharField(max_length=60)
    pulgadas = models.IntegerField()
    proveedor = models.CharField(max_length=60)
