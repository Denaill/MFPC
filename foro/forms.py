from django import forms 
from .models import Foro

class ForoForm(forms.models.ModelForm):
    
    class Meta:
        model = Foro

        fields = [
            'asunto',
            'contenido',
            'nombre_usuario',
            'correo_usuario',
            'fecha_pub',
        ]

        labels = {
            'asunto': 'Asunto de la publicación',
            'contenido': 'Contenido de la publicación',
            'nombre_usuario': 'Nombre del usuario',
            'correo_usuaro': 'Correo del usuario',
            'fecha_pub': 'Fecha de publicación',
        }

        widgets = {
            'asunto': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'correo_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pub': forms.DateInput(attrs={'class':'form-control'}),
        }