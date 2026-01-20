from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    vip = models.BooleanField(default=False)
    saldo = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    
    def __str__(self):
        return {self.username}
    
class Marca(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return {self.nombre}

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    unidades = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    vip = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='products/', null=True, blank = True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return {self.nombre}
    
    class Meta:
        unique_together = ['nombre', 'marca']

class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    unidades = models.PositiveIntegerField(default=0)
    importe = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    iva = models.DecimalField(decimal_places=2, max_digits=2, default=0.21)
    
    def __str__(self):
        return f'{self.usuario} - {self.fecha}'
    
    class Meta:
        unique_together = ['usuario', 'producto', 'fecha']