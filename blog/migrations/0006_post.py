# Generated by Django 4.0.4 on 2022-06-22 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitulo', models.CharField(max_length=100, verbose_name='Subtítulo')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de publicación')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('imagen', models.ImageField(upload_to='blog', verbose_name='Imagen')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria', verbose_name='Categoría')),
            ],
        ),
    ]
