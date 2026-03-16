from django import forms
from .models import Post, Respuesta

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Elegimos qué campos queremos mostrar en el formulario
        fields = ['titulo', 'contenido', 'categoria', 'carrera', 'archivo_adjunto']

        labels = {
            'titulo': 'Título de la Publicación',
            'categoria': 'Categoria',
            'carrera': 'Carrera Destinada',
            'contenido': 'Descripción o Dudas',
            'archivo_adjunto': 'Subir Archivo (PDF, imagen, etc.)',
        }
        
        # Opcional: Añadir clases de Bootstrap para que se vea bien
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Título de la tarea'}),
            'contenido': forms.Textarea(attrs={'class': 'textarea', 'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'searchbar-filter-input'}),
            'carrera': forms.Select(attrs={'class': 'searchbar-filter-input'}),
            'archivo_adjunto': forms.FileInput(attrs={'class': 'file-input'}),
        }

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta

        fields = ['contenido']

        labels = {
            'contenido' : 'Contenido'
        }

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'textarea', 'rows': 4}),
        }