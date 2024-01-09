from typing import Any
from django.db import models
from django.utils import timezone
import os

class Foto(models.Model):
    foto = models.ImageField(upload_to='./static/images/')
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = timezone.now()

    def __str__(self):
        return self.titulo
