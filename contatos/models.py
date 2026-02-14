from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
