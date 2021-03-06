from django.db import models

class Configuracion (models.Model):
    id_configuracion = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    logo = models.BinaryField(blank = True, null=True )

class ConfiguracionMensaje (models.Model):
    id_configuracion_mensaje = models.AutoField(primary_key=True)
    en_espera = models.TextField(default='En espera')
    en_produccion = models.TextField(default='En producción')
    cancelado = models.TextField(default='Cancelado')
    finalizado = models.TextField(default='Finalizado')
    entregado = models.TextField(default='Entregado')
    entrega = models.TextField(default='Entrega')
