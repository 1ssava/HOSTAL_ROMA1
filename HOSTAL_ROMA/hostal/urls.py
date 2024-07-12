from django.urls import path
from . import views

urlpatterns = [
    path('habitacion/', views.habitacion, name='habitacion'),
    path('hostal/', views.hostal, name='hostal'),
    path('neoHome/', views.home, name='neoHome'),
    path('widget/', views.widget, name='widget'),
    path('formsMod/', views.formsMod, name='formsMod')
    # Agrega otras rutas aquí
]
