from django.db import models

class Universidad(models.Model):
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    