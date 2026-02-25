from django import forms
from .models import Post, Respuesta

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Elegimos qué campos queremos mostrar en el formulario
        fields = ['titulo', 'contenido', 'categoria', 'carera', 'archivo_adjunto']

        labels = {
            'titulo': 'Título de la Publicación',
            'categoria': 'Categoria',
            'carera': 'Carrera Destinada',
            'contenido': 'Descripción o Dudas',
            'archivo_adjunto': 'Subir Archivo (PDF, imagen, etc.)',
        }
        
        # Opcional: Añadir clases de Bootstrap para que se vea bien
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la tarea'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'carera': forms.Select(attrs={'class': 'form-select'}),
            'archivo_adjunto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta

        fields = ['contenido']

        labels = {
            'contenido' : 'Contenido'
        }

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }