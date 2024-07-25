from django.db import models
from base.models import BaseModel

class Producto(BaseModel):

    name = models.CharField('Nombre', max_length=255, default='', blank=True)
    description = models.TextField('Descripción', default='', blank=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Cantidad', default=0, blank=True)

    def __str__(self):
        return self.name