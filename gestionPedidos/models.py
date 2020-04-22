from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50,verbose_name="La dirección")
    email = models.EmailField(blank=True,null=True)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.FloatField()

    def __str__(self): #convertir el objeto a string
        return 'El nombre es: %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio) #%s es para indicar que vamos a ingresar un valor

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()