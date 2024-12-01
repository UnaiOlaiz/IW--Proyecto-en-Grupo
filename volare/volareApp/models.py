from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    capital = models.CharField(max_length=100, default="No especificado")
    codigo = models.CharField(max_length=3)
    imagen = models.ImageField(upload_to='img/banderas',blank=True,null=True,verbose_name='Image')
    descripcion = models.TextField(default='Sin descripción')

    def __str__(self):
        return self.nombre
    
class Aeropuerto(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    tlf = models.IntegerField()
    imagen = models.ImageField(upload_to='img/',blank=True,null=True,verbose_name='Image')

    
    def __str__(self):
        return f'{self.nombre} ({self.codigo})'
    
class Aerolinea(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    aeropuertos = models.ManyToManyField(Aeropuerto, related_name='aerolineas')
    tlf = models.IntegerField()
    fundacion = models.DateField(null=True, blank=True)  
    descripcion = models.TextField(default='Sin descripción')
    flota = models.IntegerField(default=0)  
    imagen = models.ImageField(upload_to='img/',blank=True,null=True,verbose_name='Image')

    
    def __str__(self):
        return self.nombre


