from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True) # blanck true permite que el campo este vacio
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} creado por {self.user.username}'
