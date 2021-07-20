from django import forms
from django.db.models import fields
from .models import Contactos
from django.forms.widgets import Textarea

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contactos
        widgets = {
            'mensaje': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        fields = ["nombre", "apellido", "telefono", "email", "tipo_consulta", "mensaje"]
        fields = '__all__'