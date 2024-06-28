from django.contrib import admin
from .models import Habitacion, Hostal

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ("num_habitacion", "tipo_habitacion","estado")
admin.site.register(Habitacion, HabitacionAdmin)

class HostalAdmin(admin.ModelAdmin):
    list_display = ("nombre_fantasia","rol","email", "direccion")
admin.site.register(Hostal, HostalAdmin)