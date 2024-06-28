# Generated by Django 5.0.4 on 2024-06-21 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_habitacion', models.IntegerField()),
                ('tipo_habitacion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hostal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fantasia', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('id_habitacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostal.habitacion')),
            ],
        ),
    ]
