# Generated by Django 4.0.4 on 2022-06-22 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categoria_post_delete_blogmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
