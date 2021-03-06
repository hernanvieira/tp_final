from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords
# Create your models here.
#Se crean las clases de acuerdo con el diagrama de clases
class Cliente(models.Model):
    dni = models.PositiveIntegerField('DNI',primary_key=True, validators=[MinValueValidator(1000000),MaxValueValidator(99999999)])
    apellido = models.CharField('Apellido',max_length=100, blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    telefono = models.CharField('Telefono',max_length=50)
    correo = models.EmailField('Correo')
    domicilio = models.CharField('Domicilio',blank = True, null = True, max_length=500)
    reputacion = models.IntegerField('reputacion',default = 50)
    activo = models.BooleanField(default = True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'
        ordering = ['apellido']

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre

    def save(self, *args, **kwargs):
        self.apellido = (self.apellido).upper()
        self.nombre = (self.nombre).upper()
        return super(Cliente, self).save(*args, **kwargs)
