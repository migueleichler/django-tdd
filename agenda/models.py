from django.db import models


class Compromisso(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
