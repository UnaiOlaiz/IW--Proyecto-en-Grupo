from django.contrib import admin

# Register your models here.
from .models import Aerolinea, Aeropuerto, Pais
admin.site.register(Aerolinea)
admin.site.register(Aeropuerto)
admin.site.register(Pais)

