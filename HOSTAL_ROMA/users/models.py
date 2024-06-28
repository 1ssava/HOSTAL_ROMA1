from django.db import models
from django.contrib.auth.models import AbstractUser 
from universidad.models import Universidad

class CustomUser(AbstractUser):
    rol = models.CharField(max_length=30, blank=True, null=True)
    universidad = models.ForeignKey(Universidad,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    
