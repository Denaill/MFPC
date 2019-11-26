from django.db import models

# Create your models here.
class Foro(models.Model):
    asunto = models.CharField(max_length=150)
    contenido = models.CharField(max_length=500)
    nombre_usuario = models.CharField(max_length=50)
    correo_usuario = models.CharField(max_length=50)
    fecha_pub = models.CharField(max_length=50)