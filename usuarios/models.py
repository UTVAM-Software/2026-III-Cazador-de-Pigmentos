from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    vidas = models.IntegerField(default=5)
    gemas = models.IntegerField(default=0)

    nivel_maximo_desbloqueado = models.IntegerField(default=1)

    def __str__(self):
        return f"Perfil de {self.usuarios.username}"

# Create your models here.
