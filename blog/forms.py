from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    #Metaclase Meta
    class Meta:
        model = Post
        fields = [
                'id', 
                'titulo',
                'subtitulo',
                'descripcion',
                'contenido',
                'autor', 
                'fecha',
                'categoria',
                'imagen'
                ]
        
        labels = {
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'descripcion': 'Descripción',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'fecha': 'Fecha',
            'categoria': 'Categoría',
            'imagen': 'Imagen',

        }
        #Los widgets son los tipos de nuestras inputs
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 22, 'style': 'resize:none;'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Fecha dd/mm/yyyy', }),
            'imagen': forms.FileInput(),
        }
