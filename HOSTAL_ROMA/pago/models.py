from django.db import models
from users.models import CustomUser
from hostal.models import Hostal

class Pago(models.Model):
    id_estudiante = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_hostal = models.ForeignKey(Hostal, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pago {self.id_pago} - {self.monto}'