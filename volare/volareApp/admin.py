#from django.contrib import admin

# Register your models here.
#from .models import Aerolinea, Aeropuerto, Pais
#admin.site.register(Aerolinea)
#admin.site.register(Aeropuerto)
#admin.site.register(Pais)


from django.contrib import admin
from .models import Pais, Aeropuerto, Aerolinea

# Register Pais model
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capital', 'codigo', 'descripcion')  # Add useful columns in the change list
    search_fields = ['nombre', 'codigo']  # Search by name or code
    list_filter = ['capital']  # Add filtering options

admin.site.register(Pais, PaisAdmin)

# Register Aeropuerto model
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'pais', 'tlf')  # Useful columns in the change list
    search_fields = ['nombre', 'codigo']  # Search by name or code
    list_filter = ['pais']  # Filter by country
    list_display_links = ('nombre',)  # Make the 'nombre' field clickable

admin.site.register(Aeropuerto, AeropuertoAdmin)

# Register Aerolinea model
class AerolineaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'flota', 'fundacion', 'tlf')  # Useful columns in the change list
    search_fields = ['nombre']  # Search by airline name
    list_filter = ['pais', 'fundacion']  # Filter by country and foundation date
    inlines = []  # You can add inlines for related objects like Aeropuerto

admin.site.register(Aerolinea, AerolineaAdmin)
