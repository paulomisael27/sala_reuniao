from django.db import models

class SalaDeReuniao(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome