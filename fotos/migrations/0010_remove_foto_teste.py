# Generated by Django 5.0.1 on 2024-01-09 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0009_foto_teste_alter_foto_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='teste',
        ),
    ]
