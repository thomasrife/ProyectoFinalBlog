from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

#======================= MODELO CATEGORÍA  =====================================
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    descripcion = models.TextField(max_length=300, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='categoria/', blank=True, null=True )
    
    def __str__(self):
        return self.nombre

#====================== MODELO AUTOR ========================================
class Post(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    subtitulo = models.CharField(max_length=100, verbose_name='Subtítulo')
    descripcion = models.TextField(verbose_name='Descripción')
    contenido = models.TextField(verbose_name='Contenido')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    fecha = models.DateField(verbose_name='Fecha de publicación')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    imagen = models.ImageField(upload_to='blog', verbose_name='Imagen')
    
    def __str__(self):
        return self.titulo
    
    # Elimina la imagen de la carpeta 'imagenes/blog'
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


