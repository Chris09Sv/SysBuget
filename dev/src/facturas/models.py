from django.db import models
from django.conf import settings
from  django.utils import timezone


class Facturas(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    no_factura  = models.IntegerField(unique=True)
    ncf = models.IntegerField(unique=True)
    rnc = models.CharField(max_length=15)
    cliente = models.CharField(max_length=100)
    combustible = models.DecimalField(max_digits=10, decimal_places=2)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    desde = models.CharField(max_length=120)
    hasta = models.CharField(max_length=120)

