"""madeInChaco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from madeInChacoApp import views


urlpatterns = [
    path('',views.index),
    path('proyecto/',views.proyecto,name="Proyecto"),
    path('contenido/',views.contenido,name="Contenido"),
    path('recorrer/',views.recorrer,name="Recorrer"),
    path('contacto/',views.contacto,name="Contacto"),
    path('experiencia/',views.experiencia,name="Experiencia"),
    path('contenidounico/<id_contenido>',views.contenidounico,name="Contenidounico"),
      
] 

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
