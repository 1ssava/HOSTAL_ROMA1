from django.urls import path
from . import views

urlpatterns = [
    path('', views.universidad_list, name='universidad_list'),
    path('universidad/', views.universidad_create, name='universidad'),
]
