from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('habitacion/', views.habitacion, name='habitacion'),
    path('hostal/', views.hostal, name='hostal'),
    # Agrega otras rutas aquí
]
