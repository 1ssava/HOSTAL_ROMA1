from django.db import models

class Habitacion(models.Model):
    num_habitacion = models.IntegerField()
    tipo_habitacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'Habitación {self.num_habitacion} ({self.tipo_habitacion})'
class Hostal(models.Model):
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, null=True, blank=True)
    nombre_fantasia = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def str(self):
        return self.nombre_fantasia
    
# esto_es_practica    
class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.name
    
        