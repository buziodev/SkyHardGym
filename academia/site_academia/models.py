from django.db import models
from django.contrib.auth.models import User

class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='treinadores/', null=True, blank=True)

    def __str__(self):
        return self.nome


class plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    plano = models.ForeignKey(plano, on_delete=models.CASCADE)
    email = models.EmailField()
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
