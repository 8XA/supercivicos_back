from django.db import models

class Empresas(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=False)
    empresa = models.CharField('Empresa', max_length=100, blank=False)
    responsable = models.CharField('Responsable', max_length=100, blank=False)
    calle = models.CharField('Calle', max_length=100, blank=False)
    num_exterior = models.CharField('Número exterior', max_length=10, blank=False)
    num_interior = models.CharField('Número interior', max_length=10, blank=False)
    colonia = models.CharField('Colonia', max_length=100, blank=False)
    ciudad = models.CharField('Ciudad', max_length=100, blank=False)
    pais = models.CharField('Pais', max_length=100, blank=False)
    CP = models.IntegerField(null=True)
    email = models.CharField('E-mail', max_length=100, blank=False)
    telefono = models.IntegerField(null=True)
    contrasena = models.CharField('Contraseña', max_length=100, blank=False)
