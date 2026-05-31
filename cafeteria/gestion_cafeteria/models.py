from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    # auto_now_add=True guarda automáticamente la fecha y hora actual
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - Total: ${self.total}"