from typing import Any
from django.db import models
from django.utils import timezone
import os

class Foto(models.Model):
    foto = models.ImageField(upload_to='./lembrancas/fotos/static/images/')
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    data = timezone.now()


    def __str__(self):
        return self.titulo
