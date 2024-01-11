from django.db import models
from django.utils import timezone

class Pagina(models.Model):
    data_plublicacao = timezone.now()
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    titulo = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self) -> str:
        return self.titulo

