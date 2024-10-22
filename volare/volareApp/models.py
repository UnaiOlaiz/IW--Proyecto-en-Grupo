from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=3)
   
    def __str__(self):
        return self.nombre
    
class Aeropuerto(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    tlf = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} ({self.codigo})'
    
class Aerolinea(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    aeropuertos = models.ManyToManyField(Aeropuerto)
    tlf = models.IntegerField()
    
    def __str__(self):
        return self.nombre
