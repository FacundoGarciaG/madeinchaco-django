from django.contrib import admin
from gestionMICH.models import Contenidos, Contactos

# Register your models here.

class ContenidosAdmin(admin.ModelAdmin):
    list_display=("titulo","subtitulo","cuerpo","imagen","tema","fecha")
    search_fields=["titulo"]
    list_filter=("tema","fecha")
    date_hierarchy="fecha"
    readonly_fields=['fecha']

class ContactosAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","telefono","email", "tipo_de_consulta","mensaje")
    search_fields=["nombre","apellido","telefono","email"]
    list_filter=("tipo_de_consulta","fecha")
    date_hierarchy="fecha"
    readonly_fields=['fecha']

    
admin.site.register(Contenidos,ContenidosAdmin)
admin.site.register(Contactos, ContactosAdmin)


