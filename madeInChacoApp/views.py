from django.shortcuts import render
from django.template import Template,Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
from gestionMICH.models import Contenidos
from gestionMICH.forms import FormularioContacto


def layout (request):
    return render(request,"layouts/layout.html")

def layoutindex (request):
    return render(request,"layouts/layoutindex.html")

def index (request):
    return render(request,"index.html")

def proyecto (request):
    return render(request,"proyecto.html")

def contenido (request):
    contenidos=Contenidos.objects.all()
    return render(request,"contenido.html",{"contenidos":contenidos})

def recorrer (request):
    return render(request,"recorrer.html")

def contacto (request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            infoFormulario=miFormulario.cleaned_data
            return render(request,"mensajeok.html",{"respuestasFormulario":infoFormulario})
    else:
        miFormulario=FormularioContacto()
        return render(request,"contacto.html",{"form":miFormulario})


def experiencia (request):
    return render(request,"experiencia.html")

def contenidounico (request):
    return render (request,"contenidounico.html")

