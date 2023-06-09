from django.db import models
from django.conf import settings
from  django.utils import timezone
# Create your models here.
class Clientes(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length= 12)
    direccion = models.CharField(max_length=250)
    rns = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now=True)
