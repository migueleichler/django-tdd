from django.db import models


class Compromisso(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    horario = models.DateTimeField()
    local = models.CharField(max_length=100)
    observacao = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titulo
