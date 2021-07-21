from django import forms
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.forms import widgets
from django.forms.widgets import Widget
from cloudinary.models import CloudinaryField

# Create your models here.

class Contenidos(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=250)
    imagen = CloudinaryField('image',blank=True,null=True)
    tema = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='contenido'
        verbose_name_plural='contenidos'
        def __str__(self):
            return self.titulo

opciones_consultas= [
    [0, "consulta"],
    [1, "sugerencia"],
    [2, "saludo"],
    [3, "varios"]
]

class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    tipo_de_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='contacto'
        verbose_name_plural='contactos'
        def __str__(self):
            return self.nombre


