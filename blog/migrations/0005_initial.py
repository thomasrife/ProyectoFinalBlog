# Generated by Django 4.0.4 on 2022-06-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=300, verbose_name='Descripción')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='categoria/')),
            ],
        ),
    ]
