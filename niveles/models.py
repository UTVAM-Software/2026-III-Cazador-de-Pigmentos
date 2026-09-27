from django.db import models

class Nivel(models.Model):
    numero = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    instrucciones = models.TextField(blank=True)

    def __str__(self):
        return f"Nivel {self.numero} - {self.nombre}"

class Desafio(models.Model):
    TIPOS_JUEGO = [
        ('seleccion', 'Seleccion multiple (branding,Contraste, HEX)'),
        ('mezcla','Mezcla de colores (Matraces)'),
        ('rgb','Laboratorio RGB'),
        ('drag_drop','Arrastrar y soltar(Temperatura,Saturacion)'),
    ]  

    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    tipo_juego = models.CharField(max_length=20, choices=TIPOS_JUEGO)
    pregunta_objetivo = models.CharField(max_length=255)

    configuracion = models.JSONField(default=dict, help_text="Configuración específica del desafío")  

    respuesta_correcta = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nivel.nombre}: {self.pregunta_objetivo}"

    



# Create your models here.
